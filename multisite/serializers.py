from rest_framework import serializers

from api.serializers import DynamicModelSerializer
from sites.models import Site

from .models import MultiSite


class Site_Serializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()
    parent_company = serializers.StringRelatedField()

    class Meta:
        model = Site
        fields = (
            "id",
            "site_name",
            "company",
            "parent_company",
        )


class MultiSiteSerializer(DynamicModelSerializer):
    # sites = Site_Serializer(many=True)
    class Meta:
        model = MultiSite
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        if "sites" in self.fields:
            serializer = Site_Serializer
            response["sites"] = serializer(instance.sites.all(), many=True).data
        return response


# class MultiSiteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =  MultiSite
#         fields = ["id", "group_name", "group_type"]
#         model =  MultiSite
#         fields = ["id", "group_name", "group_type"]
