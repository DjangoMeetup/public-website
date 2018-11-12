
from apps.anonymous.forms import EntryForm
from apps.formality.views import evaluate_recaptcha
from apps.glaze.views import GlazeMixin
from public_website import settings
from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, TemplateView


class ErrorGlaze(GlazeMixin, TemplateView):

    template_name = 'anonymous/glaze_error.html'
    # Glaze configuration
    glaze_heading = 'Error Raised'


class HoldingView(TemplateView):

    template_name = 'anonymous/holding.html'

    def dispatch(self, request, *args, **kwargs):
        request.session['is_site_accessible'] = False
        return super().dispatch(request, *args, **kwargs)


class EntryGlaze(GlazeMixin, FormView):

    form_class = EntryForm
    success_url = reverse_lazy('anonymous:entry_granted')
    template_name = 'anonymous/glaze_entry_form.html'
    # Glaze configuration
    glaze_heading = 'Under Development Access'
    glaze_form_heading = 'Submit Credentials'
    glaze_form_action = reverse_lazy('anonymous:entry')

    def initialize_post(self, request):
        evaluate_recaptcha(request, self.glaze_external_errors)


def entry_granted(request):
    request.session['is_site_accessible'] = True
    return HttpResponseRedirect(reverse('anonymous:home'))


def is_site_accessible(request):
    """Answer true if the session has access to DjangoMeetup main website"""
    if not ('is_site_accessible' in request.session):
        request.session['is_site_accessible'] = False
    return (settings.DEBUG or request.session['is_site_accessible'])


def site_accessible(request):
    """Enable access to the site"""
    request.session['is_site_accessible'] = True


class EntryMixin:
    """Mixin class for view classes to ensure session has access"""
    def dispatch(self, request, *args, **kwargs):
        if is_site_accessible(request):
            return super().dispatch(request, *args, **kwargs)
        else:
            request.session['glaze_url'] = reverse('anonymous:entry')
            return redirect('anonymous:holding')


class LoggedInMixin(EntryMixin, AccessMixin):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            request.session['glaze_url'] = reverse('anonymous:login_required')
            return redirect('anonymous:home')
        return super().dispatch(request, *args, **kwargs)


class LoginRequiredGlaze(GlazeMixin, TemplateView):

    template_name = 'anonymous/glaze_login_required.html'
    # Glaze overlay configuration
    glaze_heading = 'Login Requried'


class HomeView(EntryMixin, TemplateView):

    template_name = 'anonymous/home.html'
