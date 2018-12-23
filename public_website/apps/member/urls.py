<<<<<<< HEAD
<<<<<<< HEAD
from django.urls import path, re_path
=======
from django.urls import path
>>>>>>> upstream/master
=======
from django.urls import path, re_path

>>>>>>> 8ef495962d88aa4d98ce223d1ca1206eafaf114b

from member import views

# Template tagging Django reference
app_name = 'member'

urlpatterns = [
    path('hub/', views.HubView.as_view(), name='hub'),
    path('login/', views.LoginGlaze.as_view(), name='login'),
    path('logout/', views.LogoutGlaze.as_view(), name='logout'),
    path('password_reset/', views.PasswordResetGlaze.as_view(), name='password_reset'),
    path('password_reset_acknowledged/', views.PasswordResetAcknowledgedGlaze.as_view(),
        name='password_reset_acknowledged'),
    path('password_reset_complete/', views.PasswordResetCompleteGlaze.as_view(), name='password_reset_complete'),
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 8ef495962d88aa4d98ce223d1ca1206eafaf114b
    re_path(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$/',
        views.PasswordResetConfirmGlaze.as_view(), name='password_reset_confirm'),
    path('password_reset_failed/', views.PasswordResetFailedGlaze.as_view(), name='password_reset_failed'),
    re_path(r'^password_reset_verification/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$/',
<<<<<<< HEAD
=======
    path('password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        views.PasswordResetConfirmGlaze.as_view(), name='password_reset_confirm'),
    path('password_reset_failed/', views.PasswordResetFailedGlaze.as_view(), name='password_reset_failed'),
    path('password_reset_verification/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
>>>>>>> upstream/master
=======

>>>>>>> 8ef495962d88aa4d98ce223d1ca1206eafaf114b
        views.password_reset_verification, name='password_reset_verification'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('signup/', views.SignupGlaze.as_view(), name='signup'),
    path('signup_acknowledged/', views.SignUpAcknowledgedGlaze.as_view(), name='signup_acknowledged'),
    path('signup_failed/', views.SignUpFailedGlaze.as_view(), name='signup_failed'),
    path('signup_verified_previously/', views.SignUpVerifiedPreviouslyGlaze.as_view(),
        name='signup_verified_previously'),
<<<<<<< HEAD
<<<<<<< HEAD
    re_path(r'^signup_verification/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$/',
=======
    path('signup_verification/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
>>>>>>> upstream/master
=======

    re_path(r'^signup_verification/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$/',
>>>>>>> 8ef495962d88aa4d98ce223d1ca1206eafaf114b
        views.signup_verification, name='signup_verification'),
    path('signup_welcome/', views.SignUpWelcomeGlaze.as_view(), name='signup_welcome'),
]
