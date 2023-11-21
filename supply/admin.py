from django.contrib import admin

from .models import Meter_detail, Current_supplies, New_supplies, UsageRates


@admin.register(Meter_detail)
class Meter_detailAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "site",
    )
    list_filter = (
        "site",
        "e_smart_meter",
        "e_related_meter",
        "e_ley_meter",
        "e_green_deal",
        "g_smart_meter",
        "g_igt_meter",
        "g_green_deal",
    )

    fieldsets = (
        (
            "Select Site",
            {
                "fields": ("site",),
            },
        ),
        (
            "Electrnic Meter Details",
            {
                "fields": (
                    "e_mpan_topline",
                    "e_mpan_bottomline",
                    "e_meter_type",
                    "e_serial_number",
                    "e_capacity",
                    "e_measurement_class",
                    "e_smart_meter",
                    "e_related_meter",
                    "e_ley_meter",
                    "e_green_deal",
                    "e_voltage",
                ),
            },
        ),
        (
            "Gas Meter Details",
            {
                "fields": (
                    "g_mpr",
                    "g_serial_number",
                    "g_smart_meter",
                    "g_igt_meter",
                    "g_green_deal",
                ),
            },
        ),
    )


@admin.register(Current_supplies)
class Current_suppliesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "site",
    )
    fieldsets = (
        (
            "Select Site",
            {
                "fields": ("site",),
            },
        ),
        (
            "Gas Meter Details",
            {
                "fields": (
                    "g_supplier",
                    "g_product",
                    "g_contract_type",
                    "g_won_date",
                    "g_contract_start_date",
                    "g_contract_end_date",
                    "g_contract_length_months",
                    "g_contract_back_date",
                    "g_supplier_reference",
                    "g_supplier_information1",
                    "g_supplier_information2",
                    "g_supplier_information3",
                    "g_agent",
                    "g_customer",
                ),
            },
        ),
        (
            "Electronic Meter Details",
            {
                "fields": (
                    "e_supplier",
                    "e_product",
                    "e_contract_type",
                    "e_won_date",
                    "e_contract_start_date",
                    "e_contract_end_date",
                    "e_contract_length_months",
                    "e_contract_back_date",
                    "e_supplier_reference",
                    "e_supplier_information1",
                    "e_supplier_information2",
                    "e_supplier_information3",
                    "e_agent",
                    "e_customer",
                ),
            },
        ),
    )


@admin.register(New_supplies)
class New_suppliesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "site",
    )

    fieldsets = (
        (
            "Select Site",
            {
                "fields": ("site",),
            },
        ),
        (
            "Gas Meter Details",
            {
                "fields": (
                    "g_supplier",
                    "g_product",
                    "g_contract_type",
                    "g_won_date",
                    "g_contract_start_date",
                    "g_contract_end_date",
                    "g_contract_length_months",
                    "g_contract_back_date",
                    "g_supplier_reference",
                    "g_supplier_information1",
                    "g_supplier_information2",
                    "g_supplier_information3",
                    "g_agent",
                    "g_customer",
                    "g_notes",
                ),
            },
        ),
        (
            "Electric Meter Details",
            {
                "fields": (
                    "e_supplier",
                    "e_product",
                    "e_contract_type",
                    "e_won_date",
                    "e_contract_start_date",
                    "e_contract_end_date",
                    "e_contract_length_months",
                    "e_contract_back_date",
                    "e_supplier_reference",
                    "e_supplier_information1",
                    "e_supplier_information2",
                    "e_supplier_information3",
                    "e_agent",
                    "e_customer",
                    "e_notes",
                    "decimal",
                ),
            },
        ),
    )


@admin.register(UsageRates)
class UsageRatesAdmin(admin.ModelAdmin):
    pass
