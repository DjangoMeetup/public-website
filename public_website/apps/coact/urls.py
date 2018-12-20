from django.conf.urls import url

from coact import views

# Template tagging Django reference
app_name = 'coact'

urlpatterns = [
    url(r'^meetup_creation$', views.MeetupCreationGlaze.as_view(), name='meetup_creation'),
]
