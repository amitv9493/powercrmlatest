
from powercrm.urls import *
from .views import *
from django.urls import path


urlpatterns = [

    path('get/company_name/', Company_Name_View.as_view(), name = 'Company_Name_View'),
    path('get/support_contact/', Support_Contact_View.as_view(), name = 'Support_Contact_View'),
    path('get/loa_template/', Loa_Template_View.as_view(), name = 'Loa_Template_View'),
    path('get/group_name/', Group_Name_View.as_view(), name = 'Group_Name_View'),

]