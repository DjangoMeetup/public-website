from django.utils.timezone import now
from django.db import models

from django.db import models
from django.template.defaultfilters import slugify

from member.models import Person
# Create your models here.


class EventGroups(models.Model):
	name = models.CharField(max_length=200, blank=True, default='Event Group', unique=True)
	details = models.CharField(max_length=1500, blank=True, null=True)

	organisor_group = models.ManyToManyField(Person, related_name='group_organisor', default='None', blank=True)
	main_user_group = models.ManyToManyField(Person, related_name='group_user', default='None', blank=True)

	class Meta:
		verbose_name_plural = 'events'

	def __str__(self):
		return '{}'.format(self.name)

class Events(models.Model):
	name = models.CharField(max_length=200, blank=True, default='Unnamed Event')
	day = models.DateTimeField(default=now, blank=True )
	details = models.CharField(max_length=1500, blank=True, null=True)
	slug = models.SlugField(max_length=255, default=name)

	group = models.ForeignKey(EventGroups, on_delete=models.CASCADE, null=True)

	attendees = models.ManyToManyField(Person, related_name='attendees', default='None', blank=True)
	organisor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name = 'event_organisor', null=True)
	address = models.CharField(max_length=250, blank=False, default='', null=True)
#	position = GeopositionField()

	class Meta:
		verbose_name_plural = 'events'

	def __str__(self):
		return '{}'.format(self.name)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Events, self).save(*args, **kwargs)