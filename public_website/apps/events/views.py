from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormView

from events.models import Events
from events.forms import EventCreationForm, GroupRegisterForm, GroupCreationForm
from glaze.views import GlazeMixin
# Create your views here.

# class EventCreationFormView(FormView, GlazeMixin):
# 	form_class = EventCreationForm

class GroupRegisterView(FormView, GlazeMixin):
	form_class = GroupRegisterForm
	template_name = 'events/event_basic_forms.html'
	#success_url = reverse_lazy('anonymous:home')
	laze_heading = 'Join Group'
	glaze_form_heading = 'Join'
	glaze_form_action = reverse_lazy('events:group_register')

class GroupCreationView(FormView, GlazeMixin):
	form_class = GroupCreationForm
	template_name = 'events/event_basic_forms.html'
	#success_url = reverse_lazy('anonymous:home')

	laze_heading = 'Create Group'
	glaze_form_heading = 'Create'
	glaze_form_action = reverse_lazy('events:group_creation')

class EventCreationView(GlazeMixin, FormView):
	form_class = EventCreationForm
	success_url = reverse_lazy('events:event_list')
	template_name = 'events/glaze_event_creation.html'
	# Glaze configuration
	glaze_heading = 'Create event'
	glaze_form_heading = 'Create'
	glaze_form_action = reverse_lazy('events:event_creation')

	def finalize_post(self, request):
		form_info = self.object
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
		print ('form saved')


class TemplateEventCreationView(GlazeMixin, TemplateView):

	template_name = 'events/event_creation.html'
    # Glaze overlay configuration
	glaze_heading = 'Event Creation'
	glaze_form_submit_name = 'Create'
	glaze_form_action = reverse_lazy('events:event_creation')

	def get(self, request):
		#getting the form and submitting it to template
		form = EventCreationForm()
		args = {'form': form}

		return render(request, self.template_name, args)

	# def initialize_post(self, request):
	# 	print ('initialized')


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
