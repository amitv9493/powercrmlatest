from rest_framework import serializers
from company.models import *
from django.contrib.auth.models import User
from .models import *
from contacts.serializers import ContactSerializer

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
    contacts = ContactSerializer()

    class Meta:
        model = Site
        fields = "__all__"
        depth = 1


class Site_Create_Serializer(serializers.ModelSerializer):
    billing_address = BillingAddressSerializer(required=False)
    site_address = SiteAddressSerializer(required=False)
    contacts = ContactSerializer(required=False)

    class Meta:
        model = Site
        fields = "__all__"
        extra_kwargs = {
            "type_of_owner": {"required": False},
            "owner_name": {"required": False},
            "current_gas_and_electricity_supplier_details": {"required": False},
        }

    # Make type_of_owner fields required=False

    # def create(self, validated_data):
    #     billing_address = validated_data.pop("billing_address")
    #     site_address = validated_data.pop("site_address")
    #     print(billing_address)
    #     print(site_address)

    #     site = Site.objects.create(**validated_data)
    #     SiteAddress.objects.create(site=site, **site_address)
    #     BillingAddress.objects.create(site=site, **billing_address)

    #     return site

    def update(self, instance, validated_data):
        billing_address_data = validated_data.pop("billing_address", {})

        site_address_data = validated_data.pop("site_address", {})

        contact_data = validated_data.pop("contacts", {})

        if site_address_data:
            site_address_serializer = self.fields["site_address"]
            site_address_serializer.update(instance.site_address, site_address_data)

        if billing_address_data:
            billing_address_serializer = self.fields["billing_address"]
            billing_address_serializer.update(
                instance.billing_address, billing_address_data
            )

        if contact_data:
            contacts_serializer = self.fields["contacts"]
            contacts_serializer.update(
                instance.contacts,
                contact_data,
            )
        return super().update(instance, validated_data)
