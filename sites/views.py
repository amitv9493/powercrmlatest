from typing import Any
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from .models import *
from company.models import *
from .serializers import *
from django.contrib.auth import get_user_model
from api.paginator import CustomPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes


User = get_user_model()
# Create your views here.

"""#######################################################
                  Company_Name_View
########################################################"""


class Company_Name_View(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = Company_Name_Serializers
    pagination_class = None


"""#######################################################
                  Support_Contact_View
########################################################"""


class Support_Contact_View(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    queryset = User.objects.all()
    pagination_class = None
    serializer_class = Support_Contact_Serializers


"""#######################################################
                  Loa_Template_View
########################################################"""


class Loa_Template_View(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    queryset = Loa_Template.objects.all()
    serializer_class = Loa_Template_Serializers
    pagination_class = None


"""#######################################################
                  Group_Name_View
########################################################"""


class Group_Name_View(ModelViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [DjangoModelPermissions, IsAdminUser]
    pagination_class = None
    queryset = group.objects.all()
    serializer_class = Group_Name_Serializers


class SiteAddressViewset(ModelViewSet):
    queryset = SiteAddress.objects.all()
    serializer_class = SiteAddressSerializer


class BillingAddressViewset(ModelViewSet):
    queryset = BillingAddress.objects.all()
    serializer_class = BillingAddressSerializer


"""#######################################################
                  Site Views
########################################################"""


class Site_view(generics.ListAPIView):
    queryset = Site.objects.select_related(
        "contacts",
        "site_address",
        "billing_address",
        "contacts",
        "company",
    )
    serializer_class = Site_Serializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["date_created"]
    ordering = ["company_id"]
    filterset_fields = [
        "group_name",
        "company",
        "support_contact",
        "loa_template",
    ]
    search_fields = [
        "parent_company",
        "site_name",
        "type_of_owner",
        "owner_name",
        "postcode_site",
        "country_site",
        "postcode_billing",
        "country_billing",
        "site_reference",
        "lead_source",
        "agent_email",
    ]

    def get_queryset(self):
        queryset = super().get_queryset()
        ids = self.request.query_params.getlist("id", None)
        if ids:
            ids = list(map(int, ids))
            queryset = queryset.filter(id__in=ids)
        return queryset

    def get_serializer_class(self):
        if self.request.query_params.get("brief", None):
            return SiteCompanySerializer
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        fields = self.request.query_params.get("fields", None)
        if fields is not None:
            fields = fields.split(",")
            kwargs["fields"] = fields
        return super().get_serializer(*args, **kwargs)

    @property
    def paginator(self):
        if self.request.query_params.get("pagination", None) == "false":
            return None
        return super().paginator


class Site_Create_view(generics.CreateAPIView):
    queryset = Site.objects.all()
    serializer_class = Site_Create_Serializer


class Site_RUD_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Site.objects.all()
    serializer_class = Site_Create_Serializer




@api_view(["GET"])
@permission_classes([])
def recent_sites(request):
    queryset = Site.objects.all().order_by("-date_created")[:10]
    return Response(Site_Serializer(queryset, many=True).data)
