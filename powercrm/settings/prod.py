import os
from datetime import timedelta

from decouple import config
from dotenv import load_dotenv

from .base import *  # noqa: F403

load_dotenv()
DEBUG = True

db = os.environ.get("db")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("NAME"),
        "USER": "aumhnwbf_root",
        "PASSWORD": config("PASSWORD"),
        "HOST": "localhost",
        "PORT": "3306",
    },
    "OPTIONS": {
        "sql_mode": "STRICT_TRANS_TABLES",
    },
}

if db:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",  # noqa: F405
        }
    }

print(db)
STATIC_ROOT = os.environ.get("STATIC_ROOT")

MEDIA_ROOT = os.environ.get("MEDIA_ROOT")

MEDIA_URL = os.environ.get("MEDIA_URL")

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
        # "rest_framework.permissions.DjangoModelPermissions",
        "rest_framework.permissions.IsAdminUser",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ],
    "DEFAULT_PAGINATION_CLASS": "api.paginator.CustomPagination",
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

CSRF_TRUSTED_ORIGINS = [
    "https://localhost:3000",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:3001",
]

CORS_ORIGIN_WHITELIST = [
    "https://localhost:3000",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://127.0.0.1:3000",
    "http://localhost:3001",
]
