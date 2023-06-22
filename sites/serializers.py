from rest_framework import serializers
from company.models import *
from django.contrib.auth.models import User
from .models import *

'''#######################################################
                  Company_Name_Serializer
########################################################'''

class Company_Name_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("id", "name")
        
'''#######################################################
                  Support_Contact_Serializer
########################################################'''

class Support_Contact_Serializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")

        
'''#######################################################
                  Loa_Template_Serializers
########################################################'''

class Loa_Template_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Loa_Template
        fields = ("id", "name", "template")
