from django.urls import path
from events import views

# Template tagging Django reference
app_name = 'events'

urlpatterns = [
    path('create-event/', views.EventCreationView.as_view(), name='event-creation'),
   ]
