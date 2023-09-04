from rest_framework import serializers
from .models import *   
from drf_writable_nested.serializers import WritableNestedModelSerializer

class Meter_Detail_Serialzer(serializers.ModelSerializer):
    class Meta:
        model = Meter_detail
        fields = "__all__"


class Current_supplies_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Current_supplies
        fields = "__all__"


class New_supplies_Serializer(serializers.ModelSerializer):
    class Meta:
        model = New_supplies
        fields = "__all__"



class SupplyDetailSerializer(WritableNestedModelSerializer):
    meter = Meter_Detail_Serialzer()
    current_supply = Current_supplies_Serializer()
    new_supply = New_supplies_Serializer()

    class Meta:
        model = Supplies
        fields = "__all__"
