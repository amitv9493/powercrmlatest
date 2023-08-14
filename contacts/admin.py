from django.contrib import admin
from .models import Contacts

# Register your models here.


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    pass
