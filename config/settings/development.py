"""
Django development settings for HRMS.
"""

from .base import *  # noqa: F401, F403

DEBUG = True

try:
    import debug_toolbar  # noqa: F401
    INSTALLED_APPS += ['debug_toolbar']  # noqa: F405
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']  # noqa: F405
except ImportError:
    pass

INTERNAL_IPS = ['127.0.0.1']

# Allow all CORS in development
CORS_ALLOW_ALL_ORIGINS = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
