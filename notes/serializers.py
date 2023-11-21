from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Note

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["select_site"] = instance.select_site.__str__()

        return data
        return data
