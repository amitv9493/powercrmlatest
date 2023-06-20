from django.contrib import admin

from .models import Business_type, Company


@admin.register(Business_type)
class Business_typeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "postcode",
        "number_of_employees",
        "registration_no",
        "business_type",
        "estimated_turnover",
        "is_macro_business",
        "account_name",
        "bank_name",
        "account_no",
        "shortcode",
        "primary_contact_first_name",
        "primary_contact_last_name",
        "contact_title",
        "primary_contact_position",
        "telephone_number",
        "primary_contact_email",
        "partner_name",
        "home_post_code",
        "partner_dob",
        "address",
        "time_at_address_years",
        "time_at_address_months",
    )
    list_filter = ("business_type", "is_macro_business", "partner_dob")
    search_fields = ("name",)

    fieldsets = (
        (
            "Company Info",
            {
                "fields": (
                    "name",
                    "number_of_employees",
                    "registration_no",
                    "business_type",
                    "estimated_turnover",
                    "is_macro_business",
                ),
            },
        ),
        (
            "Company Address",
            {
                "fields": (
                    "addressline1_company",
                    "addressline2_company",
                    "addressline3_company",
                    "postcode",
                    "country_of_company",
                ),
            },
        ),
        (
            "Bank Details",
            {
                "fields": (
                    "account_name",
                    "bank_name",
                    "account_no",
                    "shortcode",
                ),
            },
        ),
        (
            "Contact Details",
            {
                "fields": (
                    "primary_contact_first_name",
                    "primary_contact_last_name",
                    "contact_title",
                    "primary_contact_position",
                    "telephone_number",
                    "primary_contact_email",
                ),
            },
        ),
        (
            "Partner Details",
            {
                "fields": (
                    "partner_name",
                    "partner_dob",
                    "address",
                    'home_post_code',
                    "time_at_address_years",
                    "time_at_address_months",
                )
            },
        ),
    )
