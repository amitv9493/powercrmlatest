from powercrm.urls import *
from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(prefix="get/groups", viewset=Group_Name_View, basename="group")

urlpatterns = [
    path("get/company_name/", Company_Name_View.as_view(), name="Company_Name_View"),
    path(
        "get/support_contact/",
        Support_Contact_View.as_view(),
        name="Support_Contact_View",
    ),
    path("get/loa_template/", Loa_Template_View.as_view(), name="Loa_Template_View"),
    # router.urls,
    # path("get/group_name/", Group_Name_View.as_view(), name="Group_Name_View"),
] + router.urls
