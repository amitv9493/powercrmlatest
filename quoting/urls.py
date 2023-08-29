from django.urls import path
from .views import *
urlpatterns = [
    # QUOTING
    path("generate-quote/", GenerateQuoteView.as_view(), name='general-quote'),
    path("generate-quote/<int:pk>/", GenerateQuoteIDView.as_view(),name="general-quote-id"),
    path("quote-settings/", QuoteSettingView),
    path("quote-settings/<int:pk>/", QuoteSettingInstanceView, name='quote-settings'),
]
