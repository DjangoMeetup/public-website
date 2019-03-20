from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import (
    LoginView as LoginTemplate,
    LogoutView as LogoutTemplate,
    PasswordResetView as PasswordResetTemplate,
    PasswordResetDoneView as PasswordResetDoneTemplate,
    PasswordResetConfirmView as PasswordResetConfirmTemplate,
    PasswordResetCompleteView as PasswordResetCompleteTemplate,
)
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import CreateView, TemplateView

from anonymous.views import LoggedInMixin, site_accessible
from coact.email import EmailMessage
from formality.views import evaluate_recaptcha
from glaze.views import GlazeMixin
from member.forms import SignUpForm, PasswordResetForm
from member.models import Person
from member.tokens import signup_token


class SignupGlaze(GlazeMixin, CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('member:signup_acknowledged')
    template_name = 'member/glaze_signup_form.html'
    # Glaze overlay configuration
    glaze_heading = 'Account Creation'
    glaze_form_submit_name = 'Join'
    glaze_form_action = reverse_lazy('member:signup')
    is_success_glaze = True

    def initialize_post(self, request):
        evaluate_recaptcha(request, self.glaze_external_errors)

    def finalize_post(self, request):
        new_person = self.object
        new_person.save()
        self.glaze_callback_context['glaze_username'] = new_person.username
        self.glaze_callback_context['glaze_email'] = new_person.email
        subject = 'Django Meetup Account Activation'
        domain = settings.EMAIL_DOMAIN
        message = render_to_string('member/email_signup.html', {
            'person': new_person,
            'domain': domain,
            'uid': urlsafe_base64_encode(force_bytes(new_person.pk)).decode(),
            'token': signup_token.make_token(new_person),
        })
        email = EmailMessage(
            subject,
            message,
            'Django Meetup <info@djangomeetup.com>',
            [new_person.email]
        )
        email.send_async()


class SignUpAcknowledgedGlaze(GlazeMixin, TemplateView):
    template_name = 'member/glaze_signup_acknowledged.html'
    # Glaze overlay configuration
    glaze_heading = 'Account Creation Successful'


def signup_verification(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        person = Person.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Person.DoesNotExist):
        person = None

    if person is not None and signup_token.check_token(person, token):
        person.is_active = True
        person.is_email_verified = True
        person.save()
        login(request, person)
        site_accessible(request)
        request.session['glaze_url'] = reverse('member:signup_welcome')
        return redirect('member:hub')
    else:
        if person is not None and person.is_email_verified:
            site_accessible(request)
            request.session['glaze_url'] = reverse('member:signup_verified_previously')
            return redirect('anonymous:home')
        else:
            request.session['glaze_url'] = reverse('member:signup_failed')
            return redirect('anonymous:home')


class SignUpWelcomeGlaze(GlazeMixin, TemplateView):
    template_name = 'member/glaze_signup_welcome.html'
    # Glaze overlay configuration
    glaze_heading = 'Membership Verified'


class SignUpVerifiedPreviouslyGlaze(GlazeMixin, TemplateView):
    template_name = 'member/glaze_signup_verified_previously.html'
    # Glaze overlay configuration
    glaze_heading = 'Previously Verified'


class SignUpFailedGlaze(GlazeMixin, TemplateView):
    template_name = 'member/glaze_signup_failed.html'
    # Glaze overlay configuration
    glaze_heading = 'Membership Verification Failed'


class LoginGlaze(GlazeMixin, LoginTemplate):
    template_name = 'member/glaze_login_form.html'
    success_url = reverse_lazy('member:hub')
    # Glaze overlay configuration
    glaze_heading = 'Account Access'
    glaze_form_submit_name = 'Login'
    glaze_form_action = reverse_lazy('member:login')

    def initialize_post(self, request):
        evaluate_recaptcha(request, self.glaze_external_errors)

    def get_form(self):
        form = super().get_form()
        form.description = """Log into your Django Meetup account, help grow the
            Django community and enjoy our custom features."""
        return form


class LogoutGlaze(GlazeMixin, LogoutTemplate):
    template_name = 'member/glaze_logout.html'
    # Glaze overlay configuration
    glaze_heading = 'Log Out Successful'
    glaze_cancel_url = reverse_lazy('anonymous:home')


class PasswordResetGlaze(GlazeMixin, PasswordResetTemplate):
    domain = domain = settings.EMAIL_DOMAIN
    email_template_name = 'member/email_password_reset.html'
    extra_email_context = {'domain': domain}
    form_class = PasswordResetForm
    from_email = 'Django Meetup <noreply@djangomeetup.com>'
    subject_template_name = 'member/email_password_reset_subject.txt'
    success_url = reverse_lazy('member:password_reset_acknowledged')
    template_name = 'member/glaze_password_reset_form.html'
    # Glaze overlay configuration
    glaze_heading = 'Forgot Password'
    glaze_form_heading = 'Enter Membership Details'
    glaze_form_action = reverse_lazy('member:password_reset')
    is_success_glaze = True

    def initialize_post(self, request):
        evaluate_recaptcha(request, self.glaze_external_errors)


class PasswordResetAcknowledgedGlaze(GlazeMixin, PasswordResetDoneTemplate):
    template_name = 'member/glaze_password_reset_acknowledged.html'
    # Glaze overlay configuration
    glaze_heading = 'Password Reset Initiated'


def password_reset_verification(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        person = Person.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Person.DoesNotExist):
        person = None

    token_generator = default_token_generator

    password_reset_kwargs = {
        'uidb64': uidb64,
        'token': token,
    }

    if person is not None and token_generator.check_token(person, token):
        site_accessible(request)
        request.session['glaze_url'] = reverse(
            'member:password_reset_confirm',
            kwargs=password_reset_kwargs
        )
        return redirect('anonymous:home')
    else:
        request.session['glaze_url'] = reverse('member:password_reset_failed')
        return redirect('anonymous:home')


class PasswordResetConfirmGlaze(GlazeMixin, PasswordResetConfirmTemplate):
    success_url = reverse_lazy('member:password_reset_complete')
    template_name = 'member/glaze_password_reset_confirm.html'
    # Glaze overlay configuration
    glaze_heading = 'Password Reset Form'
    glaze_form_heading = 'New Password'
    glaze_form_action = None
    is_success_glaze = True

    def dispatch(self, *args, **kwargs):
        self.glaze_form_action = reverse_lazy(
            'member:password_reset_confirm',
            kwargs=kwargs
        )
        return super().dispatch(*args, **kwargs)


class PasswordResetCompleteGlaze(GlazeMixin, PasswordResetCompleteTemplate):
    template_name = 'member/glaze_password_reset_complete.html'
    # Glaze overlay configuration
    glaze_heading = 'Password Reset Complete'


class PasswordResetFailedGlaze(GlazeMixin, TemplateView):
    template_name = 'member/glaze_password_reset_failed.html'
    # Glaze overlay configuration
    glaze_heading = 'Password Reset Failed'


class HubView(LoggedInMixin, TemplateView):
    template_name = 'member/hub.html'


class ProfileView(LoggedInMixin, TemplateView):
    template_name = 'member/profile.html'
