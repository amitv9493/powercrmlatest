from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    AllUsers_view,
    BusinessTypeView,
    ChangePasswordView,
    Company_RUD_View,
    Company_view,
    CompanyDocumentView,
    CurrentElectricityProgressIDView,
    CurrentElectricityProgressView,
    CurrentGasProgressIDView,
    CurrentGasProgressView,
    GeneralDocumentView,
    LOATemplateIDView,
    LOATemplateView,
    LoginView,
    LookupViewset,
    NewElectricityProgressIDView,
    NewElectricityProgressView,
    NewGasProgressIDView,
    NewGasProgressView,
    Notes_CRUD_View,
    Notes_ListView,
    PasswordResetView,
    ProfileView,
    RegistrationView,
    SendPasswordResetView,
    SiteDocumentView,
)

router = DefaultRouter()
router.register("general-document", GeneralDocumentView, basename="general-document")
router.register("site-document", SiteDocumentView, basename="site-document")
router.register("company-document", CompanyDocumentView, basename="company-document")
router.register("lookup", LookupViewset, basename="lookup")
urlpatterns = [
    # """ROUTERS"""
    path("sites/", include("sites.urls")),
    path("multisite/", include("multisite.urls")),
    path("quote/", include("quoting.urls")),
    path("supply/", include("supply.urls")),
    path("reminder/", include("reminder.urls")),
    path("notes/", include("notes.urls")),
    # path("company/", include("company.urls")),
    # path("company/", include("company.urls")),
    # ======================================================
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("login/", LoginView.as_view(), name="loginview"),
    # path("login/", LoginView.as_view(), name="loginview"),
    path("profile/", ProfileView.as_view(), name="profileview"),
    path("changepassword/", ChangePasswordView.as_view(), name="change-password"),
    path("resetpassword/", SendPasswordResetView.as_view(), name="reset-password"),
    path("resetpassword/<uid>/<token>/", PasswordResetView.as_view()),
    # COMPANY VIEWS
    path("business-types/", BusinessTypeView.as_view()),
    path("company/", Company_view.as_view()),
    path("company/<int:pk>/", Company_RUD_View.as_view()),
    # SITES VIEW
    # Trasfered to site application
    path("users/", AllUsers_view.as_view()),
    # SUPPLY VIEWS
    # NOTES
    path("notes/", Notes_ListView.as_view()),
    path("notes/<int:pk>/", Notes_CRUD_View.as_view()),
    # COLLECTION OF ALL SUPPLIES
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
    path("company-types/", BusinessTypeView.as_view()),
    # path("orders/", Orders.as_view(), name="allorders"),
    # path("auth/", authenticate_amazon.as_view(), name="authenticate_amazon"),
    # path("auth/callback/", save_credentials.as_view(), name="save_credentials"),
    # path("hello/", hello.as_view(), name="hello_world"),
] + router.urls
