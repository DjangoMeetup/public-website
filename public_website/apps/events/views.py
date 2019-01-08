from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse, reverse_lazy

from events.models import Events
from events.forms import EventCreationForm
from glaze.views import GlazeMixin
# Create your views here.

class EventCreationView(GlazeMixin, TemplateView):

	template_name = 'events/event_creation.html'
    # Glaze overlay configuration
	glaze_heading = 'Event Creation'
	glaze_form_submit_name = 'Create'
	glaze_form_action = reverse_lazy('event:event_creation')

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


#creating a list of all the events where the user can then choose from
class EventsList(TemplateView):
	template_name='events/event_list.html'

	def get(self, request):
		event_list = []
		for event in Events.objects.all():
			event_list.append(event)
		args = {'event_list': event_list}
		return render(request, self.template_name, args)

#A more detailed view of the event itself
class EventSpecifics(TemplateView):
	template_name = 'events/event_specifics.html'

	def get(self, request, slug):
		try:
			event = Events.objects.get(slug=slug)
		except:
			return HttpResponseNotFound('<h1>Page not found</h1>')
		args = {'event': event}
		return render(request, self.template_name, args)
	def post(self, request, slug):
		user = request.user
		try:
			event = Events.objects.get(slug=slug)
		except:
			return HttpResponseNotFound('<h1>Page not found</h1>')
		if user.is_authenticated:
			event.attendees.add(request.user)
			success = True
			args = {'event': event, 'success': success}
		else:
			anonymous = True
			args = {'event': event, 'anonymous': anonymous}

		return render(request, self.template_name, args)
