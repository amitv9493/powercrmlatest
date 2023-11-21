from rest_framework.viewsets import ModelViewSet

from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    queryset = Note.objects.all()
