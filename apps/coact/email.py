
from django.core.mail import EmailMessage, send_mail
from threading import Thread


class EmailThread(Thread):

    def __init__(self, an_email):
        self.an_email = an_email
        Thread.__init__(self)

    def run(self):
        self.an_email.send()


class EmailMessageAsync(EmailMessage):

    def send_async(self, fail_silently=False):
        thread = EmailThread(self)
        thread.start()
