
from apps.glaze import views
from django.conf.urls import url


# Template tagging Django reference
app_name = 'glaze'

urlpatterns = [
    url(r'^reset_session/$', views.reset_session, name='reset_session'),
]
