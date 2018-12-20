"""
Production settings.
"""

from .base import *

# Never leave it as True!
DEBUG = False

WSGI_APPLICATION = 'public_website.wsgi.prod.application'

ALLOWED_HOSTS = ['.djangomeetup.com']

# Email configuration
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

# Django compressor
COMPRESS_CSS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

COMPRESS_JS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
    'compressor.filters.jsmin.JSMinFilter',
]
