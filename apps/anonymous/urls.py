
from apps.anonymous import views
from django.conf.urls import url
from django.views.generic.base import RedirectView


# Template tagging Django reference
app_name = "anonymous"

DEFAULT_URL = "anonymous:holding"

urlpatterns = [
    url(r"^error/$", views.ErrorGlaze.as_view(), name="error"),
    url(r"^entry/$", views.EntryGlaze.as_view(), name="entry"),
    url(r"^entry_granted/$", views.entry_granted, name="entry_granted"),
    url(r"^home/$", views.HomeView.as_view(), name="home"),
    url(r"^$", views.HoldingView.as_view(), name="holding"),
]
