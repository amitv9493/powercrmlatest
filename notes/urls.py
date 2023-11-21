from rest_framework.routers import DefaultRouter

from .views import NoteViewSet

router = DefaultRouter()
router.register("note", NoteViewSet, basename="notes")

urlpatterns = [] + router.urls
