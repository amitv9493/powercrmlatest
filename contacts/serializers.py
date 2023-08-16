from rest_framework import serializers
from .models import Contacts


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"
        fields = [
            "first_name",
            "last_name",
            "contact_title",
            "position",
            "telephone_number",
            "email",
        ]
