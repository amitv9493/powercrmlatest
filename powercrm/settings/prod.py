from .base import *
from decouple import config

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("NAME"),
        "USER": config("USER"),
        "PASSWORD": config("PASSWORD"),
        "HOST": "localhost",
        "PORT": "3306",
        "OPTIONS": {
            "raise_on_warnings": False,
        },
    }
}

ALLOWED_HOSTS = config("ALLOWED_HOSTS").split(",")
