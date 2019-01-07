from django import forms
from events.models import Events
#from django.contrib.admin.widgets import AdminSplitDateTime
from events.widgets import XDSoftDateTimePickerInput






class EventCreationForm(forms.ModelForm):

	STATE_CHOICES = (
		('ACT', 'Australian Capital Territory'),
		('NSW', 'New South Wales'),
		('NT', 'Northern Territory'),
		('QLD', 'Queensland'),
		('SA', 'South Australia'),
		('TAS', 'Tasmania'),
		('VIC', 'Victoria'),
		('WA', 'Western Australia')
		)

	address_1 = forms.CharField(
		label = 'Address Line 1',
		required=True,
		)
	suburb = forms.CharField(
		label = 'City/Suburb',
		required=False)
	postcode = forms.IntegerField(
		label = 'Postcode',
		required=True,
		max_value=9999,
		min_value=0,
		)

	state = forms.ChoiceField(
		label = 'State',
		required=True,
		choices=STATE_CHOICES
		)


	class Meta:
		model = Events
		fields = ('name', 'description', 'day')
		widgets = {
		'day': XDSoftDateTimePickerInput(),
		'description': forms.Textarea,		
		}
		input_formats = {
		'day': ['%d/%m/%Y %H:%M'],
		}
