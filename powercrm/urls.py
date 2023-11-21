from django.contrib import admin
from django.urls import include, path, re_path

from api.views import front

urlpatterns = [
    path("", front, name="front"),
    # path("api/", include("sites.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    re_path(".*", front, name="front"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
