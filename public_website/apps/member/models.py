from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils import timezone


class Person(AbstractUser):
    """
    A person and all their private state and conditions.
    Extends from the default Django User class
    """

    ### Class Variables [Person] ###############################################

    is_email_verified = models.BooleanField(default=False)
    modified_timestamp = models.DateTimeField(null=True)

    ### Accessing [Person] #####################################################

    def modified(self):
        self.modified_timestamp = timezone.now()
        self.save()

    ### Enumerating [Person] ###################################################

    def absolute_url(self):
        return reverse('member:hub', kwargs={'pk': self.pk})

    ### Printing [Person] ######################################################

    def __str__(self):
        return self.username


class Society(Group):
    """
    A group of people who share a common interest.
    """
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Societies'
        ordering = ['name']

    def __unicode__(self):
        return self.name
