from rest_framework import serializers
from .models import MultiSite
from sites.serializers import Site_Create_Serializer
from sites.models import Site

class Site_Serializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()
    parent_company = serializers.StringRelatedField()
    class Meta:
        model = Site
        fields = ("id", "site_name", "company", "parent_company",)
        
class MultiSiteSerializer(serializers.ModelSerializer):
    # sites = Site_Serializer(many=True)
    sites = serializers.SerializerMethodField
    class Meta:
        model = MultiSite
        fields = "__all__"
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        serializer = Site_Serializer
        response['sites'] = serializer(instance.sites.all(), many=True).data
        return response