from django.urls import path

from coact import views

# Template tagging Django reference
app_name = 'coact'

urlpatterns = [
    path('meetup_creation/', views.MeetupCreationGlaze.as_view(), name='meetup_creation'),
]
