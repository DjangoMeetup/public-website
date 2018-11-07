
from apps.coact import views
from django.conf.urls import url


# Template tagging Django reference
app_name = "coact"

urlpatterns = [
    url(r"^meetup_creation$", views.MeetupCreationGlaze.as_view(), name="meetup_creation"),
]
