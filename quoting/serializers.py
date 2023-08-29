from rest_framework import serializers
from .models import Generate_Quote, Generate_Group_Quote, Quoting_Settings

class GenerateQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generate_Quote
        fields = "__all__"


class QuoteSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quoting_Settings
        fields = "__all__"


class GroupQuoteSerializer(serializers.ModelSerializer):
    # group_detail = serializers.HyperlinkedIdentityField(
    #     view_name="general-quote", read_only=True, lookup_field="pk"
    # )
    group_detail = serializers.HyperlinkedRelatedField(
        view_name="general-quote",
        many=True,
        read_only=True,
        lookup_field="pk",
    )

    class Meta:
        model = Generate_Group_Quote
        fields = ["group_detail"]

