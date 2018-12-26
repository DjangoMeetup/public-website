from django.views.generic import TemplateView
from django.shortcuts import render
from events.models import Events
from events.forms import EventCreationForm
# Create your views here.

class EventCreationView(TemplateView):
	template_name = 'events/event_creation.html'


	def get(self, request):
		#getting the form and submitting it to template
		form = EventCreationForm()
		args = {'form': form}

		return render(request, self.template_name, args)

	def post(self, request):
		form = EventCreationForm()
		success = False

		if request.user.is_authenticated:
			form_info = EventCreationForm(request.POST)
			if form_info.is_valid():
				new_event = form_info.save(commit=False)
				name = form_info.cleaned_data['name']
				day = form_info.cleaned_data['day']
				
				#address
				address_1 = form_info.cleaned_data['address_1']
				suburb = form_info.cleaned_data['suburb'] + ' '
				postcode = form_info.cleaned_data['postcode']
				state = form_info.cleaned_data['state'] + ' '

				address = '{}, {}{}{}'.format(address_1, suburb, state, postcode)
				new_event.address = address


				#organisor
				organisor = request.user
				new_event.organisor = organisor

				form_info.save()
				success = True
		args = {'form': form, 'success': success}
		return render(request, self.template_name, args)
