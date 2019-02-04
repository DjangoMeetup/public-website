"""
Development settings.
"""

from .base import *

DEBUG = True

TEMPLATES[0]['OPTIONS']['debug'] = True

ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'public_website.wsgi.dev.application'

INSTALLED_APPS += [
    'debug_toolbar',
]

# Database for development.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev.sqlite3'),
    }
}

# Disable cache.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

MIDDLEWARE += [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Email backend for development
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Email configuration
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_HOST_DEBUG_ADDRESS = config('EMAIL_HOST_DEBUG_ADDRESS')

INTERNAL_IPS = ('127.0.0.1', '0.0.0.0',)
