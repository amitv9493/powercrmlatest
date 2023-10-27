from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import NoteSerializer
from .models import Note


class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
