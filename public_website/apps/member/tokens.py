from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class SignupTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, person, timestamp):
        return (
                six.text_type(person.pk)
                + six.text_type(timestamp)
                + six.text_type(person.is_email_verified)
        )


signup_token = SignupTokenGenerator()
