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
    # 'debug_toolbar.middleware.DebugPanelMiddleware',
]

# Email backend for development.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INTERNAL_IPS = ('127.0.0.1', '0.0.0.0',)
