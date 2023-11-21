from django.contrib import admin

from .models import Generate_Group_Quote, Generate_Quote, Quoting_Settings

# class Generate_QuoteAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size':'20'})},
#         models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
#     }


admin.site.register(Generate_Quote)
admin.site.register(Generate_Group_Quote)


class Quoting_SettingsAdmin(admin.ModelAdmin):
    list_display = ("allow_custom_contract_end_date",)


admin.site.register(Quoting_Settings, Quoting_SettingsAdmin)
