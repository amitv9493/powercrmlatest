from django.contrib import admin

from .models import Generate_Quote,Generate_Group_Quote,Quoting_Settings
from django.forms import TextInput, Textarea
from django.db import models



# class Generate_QuoteAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size':'20'})},
#         models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
#     }



admin.site.register(Generate_Quote)
admin.site.register(Generate_Group_Quote)

class Quoting_SettingsAdmin(admin.ModelAdmin):
 list_display=('allow_custom_contract_end_date',)
admin.site.register(Quoting_Settings,Quoting_SettingsAdmin)
