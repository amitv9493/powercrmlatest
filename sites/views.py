from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from .models import *
from company.models import *
from .serializers import *
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

'''#######################################################
                  Company_Name_View
########################################################'''

class Company_Name_View(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    queryset = Company.objects.all()
    serializer_class = Company_Name_Serializers


'''#######################################################
                  Support_Contact_View
########################################################'''

class Support_Contact_View(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    queryset = User.objects.all()
    serializer_class = Support_Contact_Serializers

    
'''#######################################################
                  Loa_Template_View
########################################################'''

class Loa_Template_View(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    queryset = Loa_Template.objects.all()
    serializer_class = Loa_Template_Serializers

    
'''#######################################################
                  Group_Name_View
########################################################'''

class Group_Name_View(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    queryset = group.objects.all()
    serializer_class = Group_Name_Serializers