from django.urls import path
from .views import (
    meter_detail_list_view,
    Current_supplies_list_view,
    New_supplies_list_view,
)

urlpatterns = [
    path("meter-detail/<int:pk>/", meter_detail_list_view.as_view()),
    path("current-supply/<int:pk>/", Current_supplies_list_view.as_view()),
    path("new-supply/<int:pk>/", New_supplies_list_view.as_view()),
]
