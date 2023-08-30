from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import MultiSiteViewSet

router = SimpleRouter()
router.register("", MultiSiteViewSet, basename="multisite")
urlpatterns = [] + router.urls
