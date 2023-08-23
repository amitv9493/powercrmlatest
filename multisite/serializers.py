from rest_framework import serializers
from .models import MultiSite
from sites.serializers import Site_Create_Serializer


class MultiSiteSerializer(serializers.ModelSerializer):
    # sites = Site_Serializer(many=True)

    class Meta:
        model = MultiSite
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["sites"] = Site_Create_Serializer(instance.sites.all(), many=True).data

        return rep
