from rest_framework import serializers
from company.models import *
from django.contrib.auth.models import User
from .models import *


"""#######################################################
                  Company_Name_Serializer
########################################################"""


class Company_Name_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("id", "name")


"""#######################################################
                  Support_Contact_Serializer
########################################################"""


class Support_Contact_Serializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


"""#######################################################
                  Loa_Template_Serializers
########################################################"""


class Loa_Template_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Loa_Template
        fields = ("id", "name", "template")


"""#######################################################
                  Group_Name_Serializers
########################################################"""


class Group_Name_Serializers(serializers.ModelSerializer):
    class Meta:
        model = group
        fields = ("id", "group_name")


class SiteAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteAddress

        fields = (
            "addressline1",
            "addressline2",
            "addressline3",
            "addressline4",
            "postcode",
            "country",
        )


class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = (
            "addressline1",
            "addressline2",
            "addressline3",
            "addressline4",
            "postcode",
            "country",
        )


"""#######################################################
                  Site_Serializers
########################################################"""


class Site_Serializer(serializers.ModelSerializer):
    billing_address = BillingAddressSerializer()
    site_address = SiteAddressSerializer()
    # general_details = serializers.SerializerMethodField()

    # support_contact = UserModel_Serializer()
    class Meta:
        model = Site
        fields = "__all__"
        depth = 1


class Site_Create_Serializer(serializers.ModelSerializer):
    billing_address = BillingAddressSerializer()
    site_address = SiteAddressSerializer()

    class Meta:
        model = Site
        fields = "__all__"

    def create(self, validated_data):
        billing_address = validated_data.pop("billing_address")
        site_address = validated_data.pop("site_address")
        print(billing_address)
        print(site_address)

        site = Site.objects.create(**validated_data)
        SiteAddress.objects.create(site=site, **site_address)
        BillingAddress.objects.create(site=site, **billing_address)

        return site

    def update(self, instance, validated_data):
        billing_address_data = validated_data.pop("billing_address", {})
        site_address_data = validated_data.pop("site_address", {})

        site_address_instance = instance.site_address
        site_address_serializer = self.fields["site_address"]
        if site_address_data:
            site_address_serializer.update(site_address_instance, site_address_data)

        billing_address_instance = instance.billing_address
        billing_address_serializer = self.fields["billing_address"]
        if billing_address_data:
            billing_address_serializer.update(
                billing_address_instance, billing_address_data
            )

        return super().update(instance, validated_data)
