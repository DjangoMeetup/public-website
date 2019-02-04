from django import forms
from django.core import validators


class EntryForm(forms.Form):
    entry_password = 'DjangoMeetup'

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'autocomplete': 'new-password',
            'placeholder': 'DjangoMeetup',
        }
    ))

    class Meta:
        fields = ('password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_instructions = """This entrance portal is merely an example of
            how to password protect a site while under development; the password
            for this site is DjangoMeetup. Try entering an incorrect password to
            view server side validation errors."""
        self.fields['password'].label = 'Entry Code'
        self.fields['password'].help_text = """Enter DjangoMeetup to gain access
            to the site; noting that the site is currently under development."""

    def clean(self):
        all_clean_data = super().clean()
        user_entry_password = all_clean_data['password']
        if user_entry_password != self.entry_password:
            raise forms.ValidationError(
                'Site entry denied, please try using DjangoMeetup'
            )
