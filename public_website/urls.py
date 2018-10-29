
from django.conf.urls import include, url


urlpatterns = [
    url(r"^", include("apps.anonymous.urls")),
    url(r"^", include("apps.glaze.urls")),
]

handler404 = "apps.anonymous.session.error"
handler500 = "apps.anonymous.session.error"
