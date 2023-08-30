from django.contrib import admin

from .models import (
    Current_gas_progress,
    Current_electricity_progress,
    New_gas_progress,
    New_electricity_progress,
)


@admin.register(Current_gas_progress)
class Current_gas_progressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "action",
        "completed",
        "priority",
        "set_status_to",
        "completed_by",
        "callback",
    )
    list_filter = ("completed", "completed_by", "callback")
    readonly_fields = ["completed_by"]

    def save_model(self, request, obj, form, change) -> None:
        obj.completed_by = request.user
        if change:
            obj.completed_by = request.user

        super().save_model(request, obj, form, change)


@admin.register(Current_electricity_progress)
class Current_electricity_progressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "action",
        "completed",
        "priority",
        "completed_by",
        "set_status_to",
        "callback",
    )
    list_filter = ("completed", "completed_by", "callback")
    readonly_fields = ["completed_by"]


@admin.register(New_gas_progress)
class New_gas_progressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "action",
        "completed",
        "priority",
        "completed_by",
        "set_status_to",
        "callback",
    )
    list_filter = ("completed", "completed_by", "callback")
    readonly_fields = ["completed_by"]


@admin.register(New_electricity_progress)
class New_electricity_progressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "action",
        "completed",
        "priority",
        "set_status_to",
        "completed_by",
        "callback",
    )
    list_filter = ("completed", "completed_by", "callback")
    readonly_fields = ["completed_by"]
