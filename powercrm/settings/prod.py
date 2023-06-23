from .base import *
from decouple import config

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("NAME"),
        "USER": "aumhnwbf_root",
        "PASSWORD": config("PASSWORD"),
        "HOST": "localhost",
        "PORT": "3306",
    }
}

STATIC_ROOT = config("STATIC_ROOT")
