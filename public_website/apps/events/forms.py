from django import forms
from events.models import Events, EventGroups
#from django.contrib.admin.widgets import AdminSplitDateTime
from events.widgets import XDSoftDateTimePickerInput


class GroupCreationForm(forms.ModelForm):
	
	class Meta:
		model = EventGroups
		fields = ('name', 'details')

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
		fields = ('name', 'details', 'day')
		widgets = {
		'day': XDSoftDateTimePickerInput(),
		'details': forms.Textarea,		
		}
		input_formats = {
		'day': ['%d/%m/%Y %H:%M'],
		}

	# def save_info(self, user):
	# 	print (True)
	# 	new_event = self.save(commit=False)
	# 	name = self.cleaned_data['name']
	# 	print (name)
	# 	day = self.cleaned_data['day']
	# 	#address
	# 	address_1 = self.cleaned_data['address_1']
	# 	suburb = self.cleaned_data['suburb'] + ' '
	# 	postcode = self.cleaned_data['postcode']
	# 	state = self.cleaned_data['state'] + ' '

	# 	address = '{}, {}{}{}'.format(address_1, suburb, state, postcode)
	# 	new_event.address = address

	# 	#organisor
	# 	organisor = user
	# 	new_event.organisor = organisor

	
	# 	self.save()
	# 