from django.contrib import admin

# Register your models here.


from .models import MultiSite


@admin.register(MultiSite)
class MultiSiteAdmin(admin.ModelAdmin):
    list_display = ("id", "group_name", "group_type")
    raw_id_fields = ("sites",)
