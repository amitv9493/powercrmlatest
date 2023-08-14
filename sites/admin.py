from django.contrib import admin
from contacts.models import Contacts
from .models import *


class ContactInline(admin.StackedInline):
    model = Contacts
    extra = 1
    fk_name = "site"
    fields = [
        "first_name",
        "last_name",
        "contact_title",
        "position",
        "telephone_number",
        "email",
    ]


class BillingAddressInline(admin.StackedInline):
    model = BillingAddress


class SiteAddressInline(admin.StackedInline):
    model = SiteAddress


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    inlines = [BillingAddressInline, SiteAddressInline, ContactInline]
    date_hierarchy = "date_created"
    ordering = ["-date_created"]
    list_display = (
        "id",
        "group_name",
        "parent_company",
        "site_name",
        "company",
        "type_of_owner",
        "owner_name",
        "current_gas_and_electricity_supplier_details",
        "site_reference",
        "support_contact",
        "lead_source",
        "notes",
        "lead_type",
        "bill_to_sent",
        "welcome_letter_send",
        "agent_email",
        "loa_header_to_use",
        "date_created",
        # "loa_template",
    )
    list_filter = (
        "company",
        "support_contact",
        "bill_to_sent",
        "welcome_letter_send",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "group_name",
                    "parent_company",
                    "site_name",
                    "company",
                    "type_of_owner",
                    "owner_name",
                    "current_gas_and_electricity_supplier_details",
                    "tenant",
                    "vacant",
                    "change_of_tenancy",
                    "customer_consent",
                ),
            },
        ),
        (
            "Our Details",
            {
                "fields": (
                    "site_reference",
                    "support_contact",
                    "lead_source",
                    "notes",
                    "lead_type",
                    "bill_to_sent",
                    "welcome_letter_send",
                ),
            },
        ),
        (
            "Letter of Authority",
            {
                "fields": (
                    "agent_email",
                    "loa_header_to_use",
                    "loa_template",
                ),
            },
        ),
    )


@admin.register(Loa_Template)
class Loa_TemplateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "template",
    )
    list_filter = ["name"]


@admin.register(group)
class groupAdmin(admin.ModelAdmin):
    pass
