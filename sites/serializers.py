from rest_framework import serializers
from company.models import *
from django.contrib.auth.models import User
from .models import *
from multisite.models import MultiSite
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
    group_site = serializers.IntegerField(write_only=True, required=False)
    class Meta:
        model = Site
        fields = "__all__"
        extra_kwargs = {
            "type_of_owner": {"required": False},
            "owner_name": {"required": False},
            "current_gas_and_electricity_supplier_details": {"required": False},
        }

        #set the contact field to its string represntation
    # Make type_of_owner fields required=False

    def create(self, validated_data):
        
        group_id = validated_data.pop("group_site", None)
        if group_id:
            try:
                group_obj = MultiSite.objects.get(id=group_id)
            except MultiSite.DoesNotExist:
                raise serializers.ValidationError({"error": "Invalid group_site"})
            
        site = super().create(validated_data)
        group_obj.sites.add(site)
                    
        return site
    
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
