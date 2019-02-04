from threading import Thread

from django.conf import settings
from django.core.mail import EmailMessage


class EmailThread(Thread):

    def __init__(self, an_email):
        self.an_email = an_email
        Thread.__init__(self)

    def run(self):
        self.an_email.send()


class EmailMessage(EmailMessage):
    """
    Enhance Django EmailMessage with threading and debug overrides for
    from_email, to, cc and bcc with dedicated debug email address.
    """

    def __init__(self, subject='', body='', from_email=None, to=None, bcc=None,
        connection=None, attachments=None, headers=None, cc=None,
        reply_to=None):
        if (settings.DEBUG):
            from_email = 'noreply@mailgun.org'
            to = [settings.EMAIL_HOST_DEBUG_ADDRESS,]
            cc = None
            bcc = None
        return super().__init__(subject=subject, body=body,
            from_email=from_email, to=to, bcc=bcc, connection=connection,
            attachments=attachments, headers=headers, cc=cc, reply_to=reply_to)

    def send_async(self, fail_silently=False):
        thread = EmailThread(self)
        thread.start()
