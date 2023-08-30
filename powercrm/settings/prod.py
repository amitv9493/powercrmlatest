from .base import *
from decouple import config

DEBUG = False
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

MEDIA_ROOT = config("MEDIA_ROOT")

MEDIA_URL = config("MEDIA_URL")


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
        "rest_framework.permissions.DjangoModelPermissions",
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
