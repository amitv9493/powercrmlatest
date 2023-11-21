from django.urls import path

from .views import (
    CompanyReminderIDView,
    CompanyReminderListView,
    GeneralReminderIDView,
    GeneralReminderListView,
    SiteReminderIDView,
    SiteReminderListView,
)

urlpatterns = [
    path("generalreminder/", GeneralReminderListView.as_view()),
    path("generalreminder/<int:pk>/", GeneralReminderIDView.as_view()),
    path("companyreminder/", CompanyReminderListView.as_view()),
    path("companyreminder/<int:pk>/", CompanyReminderIDView.as_view()),
    path("sitereminder/", SiteReminderListView.as_view()),
    path("sitereminder/<int:pk>/", SiteReminderIDView.as_view()),
]
