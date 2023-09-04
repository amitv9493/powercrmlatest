from django.contrib import admin

from .models import General_Document, Company_Document, Site_Document


@admin.register(General_Document)
class General_DocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "document", "name")
    search_fields = ("name",)


@admin.register(Company_Document)
class Company_DocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "document", "name")
    search_fields = ("name",)


@admin.register(Site_Document)
class Site_DocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "document", "name")
    search_fields = ("name",)


# @admin.register(user_credentials)
# class user_credentialsAdmin(admin.ModelAdmin):
#     list_display = ("id", "user", "code", "selling_partner_id", "updated_at")
