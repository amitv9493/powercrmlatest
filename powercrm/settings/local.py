from .base import *
from decouple import config

DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("NAME"),
        "USER": config("USER"),
        "PASSWORD": config("PASSWORD"),
        "HOST": "localhost",
        "PORT": "3306",
    }
}

INSTALLED_APPS += [
    "django_extensions",
    "knox",
]

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "api.paginator.CustomPagination",
}
