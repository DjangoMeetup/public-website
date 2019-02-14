from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse, HttpResponseBadRequest

from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormView

from events.models import Events, EventGroups, UserEventGroupManager
from events.forms import EventCreationForm, GroupRegisterForm, GroupCreationForm
from glaze.views import GlazeMixin


# note to-self, if you're getting the 405 error whilst using the mixin.
# Make sure the GlazeMixin inheritance is first, not the formview

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

    def get_form_kwargs(self, **kwargs):
        user = self.request.user
        form_kwargs = super(EventCreationView, self).get_form_kwargs()
        form_kwargs.update({
            'user': user
        })

        return form_kwargs

    def finalize_post(self, request):
        form_info = self.get_form()

        if form_info.is_valid():
            info = form_info.save(commit=False)
            name = form_info.cleaned_data['name']
            day = form_info.cleaned_data['day']
            group = form_info.cleaned_data['group']

            # address
            address_1 = form_info.cleaned_data['address_1']
            suburb = form_info.cleaned_data['suburb'] + ', '
            postcode = form_info.cleaned_data['postcode']
            state = form_info.cleaned_data['state'] + ', '

            address = '{}, {}{}{}'.format(address_1, suburb, state, postcode)
            info.address = address

            info.save()
            # organisor
            organisor = request.user
            info.organisor = organisor


# class TemplateEventCreationView(GlazeMixin, TemplateView):

# 	template_name = 'events/event_creation.html'
#     # Glaze overlay configuration
# 	glaze_heading = 'Event Creation'
# 	glaze_form_submit_name = 'Create'
# 	glaze_form_action = reverse_lazy('events:event_creation')

# 	def get(self, request):
# 		#getting the form and submitting it to template
# 		form = EventCreationForm()
# 		args = {'form': form}

# 		return render(request, self.template_name, args)


# creating a list of all the events where the user can then choose from
class EventsList(TemplateView):
    template_name = 'events/event_list.html'

    def get(self, request):
        # retrieve's and lists all the events
        event_list = []
        for event in Events.objects.all():
            event_list.append(event)
        args = {'event_list': event_list}

        return render(request, self.template_name, args)


# A more detailed view of the event itself
class EventSpecifics(TemplateView):
    template_name = 'events/event_specifics.html'

    def get(self, request, slug):
        is_group = False

        # google_url

        # Try and get the event corresponding to the slug.
        # get or 404 causes other problems, so I reccommend you don't try and use it
        try:
            event = Events.objects.get(slug=slug)
            got_event = True
        except:
            return HttpResponseNotFound('<h1>Page not found</h1>')

        # if the user is part in the event pass a true variable to the template
        if got_event:
            # google urls

            address_str = str(event.address)
            position_no_comma = address_str.replace(',', '%2C')
            position_no_space = position_no_comma.replace(' ', '+')
            google_url = "https://www.google.com/maps/search/" + position_no_space
            print(google_url)
            args = {'event': event, 'google_url': google_url}
            # get a list of all the groups the user is in
            user_groups = [_event for _event in UserEventGroupManager().get_queryset(request).all()]
            if event.group in user_groups:
                is_group = True
                args['is_group'] = is_group

        return render(request, self.template_name, args)

    def post(self, request, slug):
        user = request.user

        try:
            event = Events.objects.get(slug=slug)
            got_event = True
        except:
            return HttpResponseNotFound('<h1>Page not found</h1>')

        if got_event:
            address_str = str(event.address)
            position_no_comma = address_str.replace(',', '%2C')
            position_no_space = position_no_comma.replace(' ', '+')
            google_url = "https://www.google.com/maps/search/" + position_no_space
            print(google_url)
            args = {'event': event, 'google_url': google_url}
            # get a list of all the groups the user is in
            user_groups = [_event for _event in UserEventGroupManager().get_queryset(request).all()]
            if event.group in user_groups:
                args['is_group'] = True

        if user.is_authenticated:
            event.attendees.add(request.user)
            success = True
            args['success'] = success
        else:
            anonymous = True
            args['anonymous'] = anonymous

        return render(request, self.template_name, args)
