
from django.conf.urls import include, url, handler404, handler500


urlpatterns = [
    url(r"^", include("apps.anonymous.urls")),
]
