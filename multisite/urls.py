from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register("", MultiSiteViewSet, basename="multisite")
urlpatterns = [
    path('multisitelist/', multisite.as_view(), name = "multisitelist")
    
    ] + router.urls
