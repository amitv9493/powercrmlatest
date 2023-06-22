from .base import *
from decouple import config

DATABASES = {
    "default": {
        "ENGINE": "mysql.connector.django",
        "NAME": config("NAME"),
        "USER": config("USER"),
        "PASSWORD": config("PASSWORD"),
        "HOST": "localhost",
        "PORT": "3306",
    }
}
