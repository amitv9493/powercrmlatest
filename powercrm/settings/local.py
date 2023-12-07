import os
from pathlib import Path

from .base import *  # noqa: F403

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

INSTALLED_APPS += [  # noqa: F405
    "django_extensions",
    # "silk",
    # "debug_toolbar",
]

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "api.paginator.CustomPagination",
}


CSRF_COOKIE_SAMESITE = "Strict"
SESSION_COOKIE_SAMESITE = "Strict"
CSRF_COOKIE_HTTPONLY = False  # False since we will grab it via universal-cookies
SESSION_COOKIE_HTTPONLY = True

# MIDDLEWARE.insert(0, 'silk.middleware.SilkyMiddleware')

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
SILKY_PYTHON_PROFILER = True


LOOKUP_EMAIL = os.environ.get("lookup_email", "")
LOOKUP_PASSWORD = os.environ.get("lookup_password", "")
