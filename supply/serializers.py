from rest_framework import serializers
from .models import *
from drf_writable_nested.serializers import WritableNestedModelSerializer
from api.serializers import DynamicModelSerializer


class NewSupplierGASUsage(serializers.Serializer):
    stading_charge = serializers.DecimalField(
        max_digits=6, decimal_places=4, required=False
    )
    standing_charge_uplift = serializers.DecimalField(
        max_digits=6, decimal_places=4, required=False
    )
    rate = serializers.DecimalField(max_digits=6, decimal_places=4, required=False)
    unit_rate_uplift = serializers.DecimalField(
        max_digits=6, decimal_places=4, required=False
    )
    annual_usage = serializers.IntegerField(required=False)


class NewSupplierELECTRICUsage(serializers.Serializer):
    stading_charge = serializers.DecimalField(
        max_digits=6, decimal_places=4, required=False
    )
    standing_charge_uplift = serializers.DecimalField(
        max_digits=6, decimal_places=4, required=False
    )
    unit_rate_uplift = serializers.DecimalField(
        max_digits=6, decimal_places=4, required=False
    )
    kva_rate = serializers.DecimalField(max_digits=6, decimal_places=4, required=False)
    feed_in_tariff = serializers.DecimalField(
        max_digits=6, decimal_places=4, required=False
    )
    annual_day_usage = serializers.IntegerField(required=False)
    day_rate = serializers.DecimalField(max_digits=6, decimal_places=4, required=False)
    night_rate = serializers.DecimalField(
        max_digits=6, decimal_places=4, required=False
    )
    annual_night_usage = serializers.IntegerField(required=False)

    evening_rate = serializers.DecimalField(
        max_digits=6, decimal_places=4, required=False
    )
    annual_evening_usage = serializers.IntegerField(required=False)


class CurrentSupplyGASUsage(serializers.Serializer):
    stading_charge = serializers.DecimalField(
        max_digits=6, decimal_places=4, required=False
    )
    standing_charge_uplift = serializers.DecimalField(
        max_digits=6, decimal_places=4, required=False
    )
    unit_rate_uplift = serializers.DecimalField(
        max_digits=6, decimal_places=4, required=False
    )
    rate = serializers.DecimalField(max_digits=6, decimal_places=4, required=False)
    annual_usage = serializers.IntegerField(required=False)


class CurrentSupplyELECTRICUsage(serializers.Serializer):
    stading_charge = serializers.DecimalField(
        max_digits=6, decimal_places=4, required=False
    )
    standing_charge_uplift = serializers.DecimalField(
        max_digits=6, decimal_places=4, required=False
    )
    unit_rate_uplift = serializers.DecimalField(
        max_digits=6, decimal_places=4, required=False
    )
    kva_rate = serializers.DecimalField(max_digits=6, decimal_places=4, required=False)
    feed_in_tariff = serializers.DecimalField(
        max_digits=6, decimal_places=4, required=False
    )
    annual_day_usage = serializers.IntegerField(required=False)
    day_rate = serializers.DecimalField(max_digits=6, decimal_places=4, required=False)
    night_rate = serializers.DecimalField(
        max_digits=6, decimal_places=4, required=False
    )
    annual_night_usage = serializers.IntegerField(required=False)


class UsageRateSerializer(DynamicModelSerializer):
    class Meta:
        model = UsageRates
        fields = "__all__"


class Meter_Detail_Serialzer(serializers.ModelSerializer):
    class Meta:
        model = Meter_detail
        exclude = (
            "site",
            "id",
        )


class Current_supplies_Serializer(serializers.ModelSerializer):
    gas_usage_rate = CurrentSupplyGASUsage(write_only=True, required=False)
    electric_usage_rate = CurrentSupplyELECTRICUsage(write_only=True, required=False)

    class Meta:
        model = Current_supplies
        exclude = (
            "site",
            "id",
        )

    def update(self, instance, validated_data):
        gas_usage_rate = validated_data.pop("gas_usage_rate", None)
        electric_usage_rate = validated_data.pop("electric_usage_rate", None)
        gas_usage_rate_instance = instance.usage_rates.filter(usage_type="GAS").first()
        elec_usage_rate_instance = instance.usage_rates.filter(
            usage_type="ELECTRIC"
        ).first()

        if gas_usage_rate and gas_usage_rate_instance:
            for key, value in gas_usage_rate.items():
                setattr(gas_usage_rate_instance, key, value)

            gas_usage_rate_instance.save(update_fields=list(gas_usage_rate.keys()))
        elif gas_usage_rate:
            gas_usage_rate["usage_type"] = "GAS"
            instance.usage_rates.create(**gas_usage_rate)

        if electric_usage_rate and elec_usage_rate_instance:
            for key, value in electric_usage_rate.items():
                setattr(elec_usage_rate_instance, key, value)

            elec_usage_rate_instance.save(
                update_fields=list(electric_usage_rate.keys())
            )
        elif electric_usage_rate:
            electric_usage_rate["usage_type"] = "ELECTRIC"

            instance.usage_rates.create(**electric_usage_rate)

        return super().update(instance, validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        gas_usages_rate_instance = (
            instance.usage_rates.all().filter(usage_type="GAS").first()
        )
        electric_usages_rate_instance = (
            instance.usage_rates.all().filter(usage_type="ELECTRIC").first()
        )

        if gas_usages_rate_instance:
            data["gas_usage_rate"] = CurrentSupplyGASUsage(
                gas_usages_rate_instance
            ).data
        if electric_usages_rate_instance:
            data["electric_usage_rate"] = CurrentSupplyELECTRICUsage(
                electric_usages_rate_instance
            ).data

        return data


class New_supplies_Serializer(serializers.ModelSerializer):
    gas_usage_rate = NewSupplierGASUsage(write_only=True, required=False)
    electric_usage_rate = NewSupplierELECTRICUsage(write_only=True, required=False)

    class Meta:
        model = New_supplies
        exclude = (
            "site",
            "id",
        )

    def update(self, instance, validated_data):
        gas_usage_rate = validated_data.pop("gas_usage_rate", None)
        electric_usage_rate = validated_data.pop("electric_usage_rate", None)
        gas_usage_rate_instance = instance.usage_rates.filter(usage_type="GAS").first()
        elec_usage_rate_instance = instance.usage_rates.filter(
            usage_type="ELECTRIC"
        ).first()

        if gas_usage_rate and gas_usage_rate_instance:
            for key, value in gas_usage_rate.items():
                setattr(gas_usage_rate_instance, key, value)

            gas_usage_rate_instance.save(update_fields=list(gas_usage_rate.keys()))
        elif gas_usage_rate:
            gas_usage_rate["usage_type"] = "GAS"
            instance.usage_rates.create(**gas_usage_rate)

        if electric_usage_rate and elec_usage_rate_instance:
            for key, value in electric_usage_rate.items():
                setattr(elec_usage_rate_instance, key, value)

            elec_usage_rate_instance.save(
                update_fields=list(electric_usage_rate.keys())
            )
        elif electric_usage_rate:
            electric_usage_rate["usage_type"] = "ELECTRIC"

            instance.usage_rates.create(**electric_usage_rate)

        return super().update(instance, validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        gas_usages_rate_instance = (
            instance.usage_rates.all().filter(usage_type="GAS").first()
        )
        electric_usages_rate_instance = (
            instance.usage_rates.all().filter(usage_type="ELECTRIC").first()
        )
        # usage_rates = {}

        if gas_usages_rate_instance:
            data["gas_usage_rate"] = NewSupplierGASUsage(gas_usages_rate_instance).data
        if electric_usages_rate_instance:
            data["electric_usage_rate"] = NewSupplierELECTRICUsage(
                electric_usages_rate_instance
            ).data
        return data


class SupplyDetailSerializer(WritableNestedModelSerializer):
    meter = Meter_Detail_Serialzer()
    current_supply = Current_supplies_Serializer()
    new_supply = New_supplies_Serializer()

    class Meta:
        model = Supplies
        fields = "__all__"
