from django.views.generic import TemplateView

from glaze.views import GlazeMixin


class MeetupCreationGlaze(GlazeMixin, TemplateView):
    template_name = 'coact/glaze_meetup_creation.html'
    # Glaze overlay configuration
    glaze_heading = 'Start a Django Meetup'
