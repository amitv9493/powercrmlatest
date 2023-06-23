from django.contrib import admin

from .models import Loa_Template, Site, group


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
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
            "Site Address",
            {
                "fields": (
                    "postcode_site",
                    "addressline1_site",
                    "addressline2_site",
                    "addressline3_site",
                    "addressline4_site",
                    "country_site",
                ),
            },
        ),
        (
            "Billing Address",
            {
                "fields": (
                    "postcode_billing",
                    "addressline1_billing",
                    "addressline2_billing",
                    "addressline3_billing",
                    "addressline4_billing",
                    "country_billing",
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
