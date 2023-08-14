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
]

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "api.paginator.CustomPagination",
}
