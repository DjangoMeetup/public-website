
from apps.anonymous import views
from django.conf.urls import url
from django.views.generic.base import RedirectView


# Template tagging Django reference
app_name = "anonymous"

urlpatterns = [
    url(r"^$", views.HoldingView.as_view(), name="holding"),
]
