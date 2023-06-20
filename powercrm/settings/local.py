from .base import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "powercrm",
        "USER": "root",
        "PASSWORD": "amitv9493",
        "HOST": "localhost",
        "PORT": "3306",
    }
}

INSTALLED_APPS += [
    "django_extensions",
]
