from django.contrib import admin
from .models import General_Reminder,Company_Reminder,Site_Reminder

# Register your models here.
admin.site.register(General_Reminder)
admin.site.register(Company_Reminder)
admin.site.register(Site_Reminder)

