from django import forms
from events.models import Events, EventGroups
#from django.contrib.admin.widgets import AdminSplitDateTime
from events.widgets import XDSoftDateTimePickerInput


class GroupCreationForm(forms.ModelForm):
	
	class Meta:
		model = EventGroups
		fields = ('name', 'details')

		widgets = {
		'details': forms.Textarea,		
		}

class GroupRegisterForm(forms.Form):
	groups = forms.ModelMultipleChoiceField(queryset=EventGroups.objects.all())



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
		label = 'Address',
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
		fields = ('name', 'details', 'day', 'group')

		widgets = {
		'day': XDSoftDateTimePickerInput(),
		'details': forms.Textarea,		
		}
		input_formats = {
		'day': ['%d/%m/%Y %H:%M'],
		}
	
	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user', None)

		super(EventCreationForm, self).__init__(*args, **kwargs)
		self.fields['group'].queryset = EventGroups.objects.filter(main_user_group=user)
