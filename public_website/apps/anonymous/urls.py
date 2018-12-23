from public_website.apps.anonymous import views
from django.urls import path
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> upstream/master
=======

>>>>>>> 8ef495962d88aa4d98ce223d1ca1206eafaf114b

# Template tagging Django reference
app_name = 'anonymous'

DEFAULT_URL = 'anonymous:holding'

urlpatterns = [
    path('error/', views.ErrorGlaze.as_view(), name='error'),
    path('entry/', views.EntryGlaze.as_view(), name='entry'),
    path('entry_granted/', views.entry_granted, name='entry_granted'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('login_required/', views.LoginRequiredGlaze.as_view(), name='login_required'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('/', views.HoldingView.as_view(), name='holding'),
=======
    path('', views.HoldingView.as_view(), name='holding'),
>>>>>>> upstream/master
=======

    path('', views.HoldingView.as_view(), name='holding'),

>>>>>>> 8ef495962d88aa4d98ce223d1ca1206eafaf114b
]

