
from apps.member.models import Person
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    PasswordResetForm as PasswordResetFormTemplate
)
from django.core.validators import RegexValidator

import threading


class SignUpForm(UserCreationForm):

    email = forms.EmailField(
        max_length=254,
        help_text="Valid email required for member authentication.")

    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.description = """Create a Django Meetup account, help grow the
            Django community and enjoy our custom features."""
        self.fields["password2"].label = "Confirm"

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data["email"]
        username = all_clean_data["username"]
        if email and Person.objects.filter(email=email).exclude(username=username).exists():
            self.add_error('email', u"Email is already associated with another account")


class PasswordResetForm(PasswordResetFormTemplate):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.description = """Submit your account email for instructions on how
            to reset your password. You will need to complete within 1 hour."""

    def send_mail(self, subject_template_name, email_template_name,
            context, from_email, to_email, html_email_template_name=None):
        send_email_thread = threading.Thread(
            target=super().send_mail,
            args=[
                subject_template_name,
                email_template_name,
                context,
                "Django Meetup <info@djangomeetup.com>",
                to_email
            ]
        )
        send_email_thread.start()
