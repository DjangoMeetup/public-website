from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()
urlpatterns = []

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = [
    # Admin.
    path('admin/', admin.site.urls),

    path('coact/', include('coact.urls')),
    path('member/', include('member.urls')),
	path('events/', include('events.urls')),
    path('', include('anonymous.urls')),
    path('', include('glaze.urls')),
]

handler404 = 'anonymous.session.error'
handler500 = 'anonymous.session.error'
