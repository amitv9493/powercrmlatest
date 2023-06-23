from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("general-document", GeneralDocumentView, basename="general-document")
router.register("site-document", SiteDocumentView, basename="site-document")
router.register("company-document", CompanyDocumentView, basename="company-document")

urlpatterns = [
    # """ROUTERS"""
    path("sites/", include("sites.urls")),
    # path("company/", include("company.urls")),
    # ======================================================
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("login/", LoginView.as_view(), name="loginview"),
    path("profile/", ProfileView.as_view(), name="profileview"),
    path("changepassword/", ChangePasswordView.as_view(), name="change-password"),
    path("resetpassword/", SendPasswordResetView.as_view(), name="reset-password"),
    path("resetpassword/<uid>/<token>/", PasswordResetView.as_view()),
    # COMPANY VIEWS
    path("business-types/", BusinessTypeView.as_view()),
    path("company/", Company_view.as_view()),
    path("company/<int:pk>/", Company_RUD_View.as_view()),
    # SITES VIEW
    path("site/", Site_view.as_view()),
    path("site/<int:pk>/", Site_RUD_View.as_view()),
    path("users/", AllUsers_view.as_view()),
    # SUPPLY VIEWS
    path("meter-detail/<int:pk>/", meter_detail_list_view.as_view()),
    path("current-supply/<int:pk>/", Current_supplies_list_view.as_view()),
    path("new-supply/<int:pk>/", New_supplies_list_view.as_view()),
    # NOTES
    path("notes/", Notes_ListView.as_view()),
    path("notes/<int:pk>/", Notes_CRUD_View.as_view()),
    # REMINDERS
    path("generalreminder/", GeneralReminderListView.as_view()),
    path("generalreminder/<int:pk>/", GeneralReminderIDView.as_view()),
    path("companyreminder/", CompanyReminderListView.as_view()),
    path("companyreminder/<int:pk>/", CompanyReminderIDView.as_view()),
    path("sitereminder/", SiteReminderListView.as_view()),
    path("sitereminder/<int:pk>/", SiteReminderIDView.as_view()),
    # COLLECTION OF ALL SUPPLIES
    path("supplyview/<int:site_id>/", SupplyView),
    # QUOTING
    path("generalquote/", GenerateQuoteListView.as_view()),
    path("generalquote/<int:pk>/", GenerateQuoteIDView.as_view()),
    path("quote-settings/", QuoteSettingView),
    path("quote-settings/<int:pk>/", QuoteSettingInstanceView),
    path("general-quote/", GeneralQuoteView.as_view()),
    path("general-quote/<int:pk>/", GeneralQuoteIDView.as_view(), name="general-quote"),
    path("group-quote/", GroupQuoteView.as_view()),
    path("loa-templates/", LOATemplateView.as_view()),
    path("loa-templates/<int:pk>/", LOATemplateIDView.as_view()),
    # PROGRESS VIEW
    path("current-gas/", CurrentGasProgressView.as_view()),
    path("current-gas/<int:pk>/", CurrentGasProgressIDView.as_view()),
    #
    path("current-ele/", CurrentElectricityProgressView.as_view()),
    path("current-ele/<int:pk>/", CurrentElectricityProgressIDView.as_view()),
    #
    path("new-gas/", NewGasProgressView.as_view()),
    path("new-gas/<int:pk>/", NewGasProgressIDView.as_view()),
    #
    path("new-ele/", NewElectricityProgressView.as_view()),
    path("new-ele/<int:pk>/", NewElectricityProgressIDView.as_view()),
    #
] + router.urls
