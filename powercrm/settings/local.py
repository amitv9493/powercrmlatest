from .base import *
from decouple import config

DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("NAME"),
        "USER": config("USER"),
        "PASSWORD": config("PASSWORD"),
        "HOST": "localhost",
        "PORT": "5432",
    }
}

INSTALLED_APPS += [
    "django_extensions",
    "knox",
    "silk",
]

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "api.paginator.CustomPagination",
}


CSRF_COOKIE_SAMESITE = "Strict"
SESSION_COOKIE_SAMESITE = "Strict"
CSRF_COOKIE_HTTPONLY = False  # False since we will grab it via universal-cookies
SESSION_COOKIE_HTTPONLY = True

MIDDLEWARE.insert(0, 'silk.middleware.SilkyMiddleware')


SILKY_PYTHON_PROFILER =True