from django.contrib import admin

from .models import MultiSite

# Register your models here.


@admin.register(MultiSite)
class MultiSiteAdmin(admin.ModelAdmin):
    list_display = ("id", "group_name", "group_type")
    raw_id_fields = ("sites",)
