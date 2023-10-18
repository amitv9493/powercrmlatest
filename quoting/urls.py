from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix="group-quote", viewset=GroupQuoteView, basename="general-quote")

urlpatterns = [
    # QUOTING
    path("generate-quote/", GenerateQuoteView.as_view(), name="general-quote"),
    path(
        "generate-quote/<int:pk>/",
        GenerateQuoteIDView.as_view(),
        name="general-quote-id",
    ),
    path("quote-settings/", QuoteSettingView),
    path("quote-settings/<int:pk>/", QuoteSettingInstanceView, name="quote-settings"),
    # path("group-quote/", GroupQuoteView.as_view(), name='group-quote'),
    path("recent-quotes/", recent_quotes, name="recent-quotes"),
    path(
        "generate-quote/multisite/<int:pk>/",
        Multisite_Quoting.as_view(),
        name="multisite_detail",
    ),
] + router.urls
