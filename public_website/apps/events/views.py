from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormView

from events.models import Events, EventGroups
from events.forms import EventCreationForm, GroupRegisterForm, GroupCreationForm
from glaze.views import GlazeMixin


#note to-self, if you're getting the 405 error whilst using the mixin. 
#Make sure the GlazeMixin inheritance is first, not the formview

class GroupRegisterView(GlazeMixin, FormView):
	form_class = GroupRegisterForm
	template_name = 'events/event_basic_forms.html'
	success_url = reverse_lazy('events:event_list')
	glaze_heading = 'Join Group'
	glaze_form_heading = 'Join'
	is_success = True
	glaze_form_action = reverse_lazy('events:group_register')

	def finalize_post(self, request):

		form_info = GroupRegisterForm(request.POST)
		if form_info.is_valid():
			groups = form_info.cleaned_data['groups']
			for group in groups:
				group.main_user_group.add(request.user)

	

class GroupCreationView(GlazeMixin, FormView):
	form_class = GroupCreationForm
	template_name = 'events/event_basic_forms.html'
	success_url = reverse_lazy('events:event_list')

	laze_heading = 'Create Group'
	glaze_form_heading = 'Create'
	glaze_form_action = reverse_lazy('events:group_creation')

	def finalize_post(self, request):

		form_info = GroupCreationForm(request.POST)
		if form_info.is_valid():
			form_info.save()
			name = form_info.cleaned_data['name']
			
			new_group = EventGroups.objects.get(name=name)
			new_group.organisor_group.add(request.user)

class EventCreationView(GlazeMixin, FormView):
	form_class = EventCreationForm
	success_url = reverse_lazy('events:event_list')
	template_name = 'events/glaze_event_creation.html'
	# Glaze configuration
	glaze_heading = 'Create event'
	glaze_form_heading = 'Create'
	glaze_form_action = reverse_lazy('events:event_creation')

	def finalize_post(self, request):
		form_info = EventCreationForm(request.POST)
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
