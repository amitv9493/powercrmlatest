from powercrm.urls import *
from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(prefix="groups", viewset=Group_Name_View, basename="group")
router.register("get/siteaddress", SiteAddressViewset, basename="site-address")
router.register("get/billingaddress", BillingAddressViewset, basename="billing-address")


urlpatterns = [
    path("get/site/", Site_view.as_view(),name="site-list"),
    path("create/site/", Site_Create_view.as_view()),
    path("update/site/<int:pk>/", Site_RUD_View.as_view()),
    path("get/company_name/", Company_Name_View.as_view(), name="Company_Name_View"),
    path(
        "get/support_contact/",
        Support_Contact_View.as_view(),
        name="Support_Contact_View",
    ),
    path("get/loa_template/", Loa_Template_View.as_view(), name="Loa_Template_View"),
] + router.urls
