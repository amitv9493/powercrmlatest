from rest_framework import serializers

# from sites.serializers import Site_Create_Serializer
from multisite.serializers import Site_Serializer

from .models import Generate_Group_Quote, Generate_Quote, Quoting_Settings


class GenerateQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generate_Quote
        fields = "__all__"
        # depth =1

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["site"] = Site_Serializer(instance.site).data
        return data


class QuoteSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quoting_Settings
        fields = "__all__"


class GroupQuoteGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generate_Group_Quote
        fields = "__all__"
        depth = 1


class GroupQuotePOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generate_Group_Quote
        fields = "__all__"


class Multisite_QuotingSerializer(serializers.Serializer):
    supplier = serializers.CharField()
    product = serializers.CharField()
    term = serializers.IntegerField()
    day_rate = serializers.FloatField()
    night_rate = serializers.FloatField()
    standing_charge = serializers.FloatField()
    kva_charge = serializers.FloatField()
    additional_charge = serializers.FloatField()
    extra_info = serializers.CharField()
    up_lift = serializers.FloatField()
    rates_already_include_at_uplift = serializers.BooleanField()

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        multisite_object = self.context.get("multisite")

        return multisite_object
        return multisite_object
