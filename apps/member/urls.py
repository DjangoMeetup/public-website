
from apps.member import views
from django.conf.urls import url


# Template tagging Django reference
app_name = 'member'

urlpatterns = [
    url(r'^hub$', views.HubView.as_view(), name='hub'),
    url(r'^login$', views.LoginGlaze.as_view(), name='login'),
    url(r'^logout$', views.LogoutGlaze.as_view(), name='logout'),
    url(r'^password_reset$', views.PasswordResetGlaze.as_view(), name='password_reset'),
    url(r'^password_reset_acknowledged$', views.PasswordResetAcknowledgedGlaze.as_view(), name='password_reset_acknowledged'),
    url(r'^password_reset_complete$', views.PasswordResetCompleteGlaze.as_view(), name='password_reset_complete'),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.PasswordResetConfirmGlaze.as_view(), name='password_reset_confirm'),
    url(r'^password_reset_failed$', views.PasswordResetFailedGlaze.as_view(), name='password_reset_failed'),
    url(r'^password_reset_verification/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_verification, name='password_reset_verification'),
    url(r'^profile$', views.ProfileView.as_view(), name='profile'),
    url(r'^signup$', views.SignupGlaze.as_view(), name='signup'),
    url(r'^signup_acknowledged$', views.SignUpAcknowledgedGlaze.as_view(), name='signup_acknowledged'),
    url(r'^signup_failed$', views.SignUpFailedGlaze.as_view(), name='signup_failed'),
    url(r'^signup_verified_previously$', views.SignUpVerifiedPreviouslyGlaze.as_view(), name='signup_verified_previously'),
    url(r'^signup_verification/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.signup_verification, name='signup_verification'),
    url(r'^signup_welcome$', views.SignUpWelcomeGlaze.as_view(), name='signup_welcome'),
]
