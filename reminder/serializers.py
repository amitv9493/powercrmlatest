from rest_framework import serializers

from .models import *

class CompanyReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_Reminder
        fields = "__all__"


class SiteReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site_Reminder
        fields = "__all__"


class GeneralReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = General_Reminder
        fields = "__all__"