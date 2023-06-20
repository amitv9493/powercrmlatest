from django.contrib import admin
from .models import *


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['select_site','site_notes', 'company_notes']
