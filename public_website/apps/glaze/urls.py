from django.urls import path

from glaze import views

# Template tagging Django reference
app_name = 'glaze'

urlpatterns = [
    path('reset_session/', views.reset_session, name='reset_session'),
]
