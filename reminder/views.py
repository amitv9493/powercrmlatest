from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Company_Reminder, General_Reminder, Site_Reminder
from .serializers import (
    CompanyReminderSerializer,
    GeneralReminderSerializer,
    SiteReminderSerializer,
)

# Create your views here.


class GeneralReminderListView(generics.ListCreateAPIView):
    queryset = General_Reminder.objects.all()
    serializer_class = GeneralReminderSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["active"]


class GeneralReminderIDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = General_Reminder.objects.all()
    serializer_class = GeneralReminderSerializer


class CompanyReminderListView(generics.ListCreateAPIView):
    queryset = Company_Reminder.objects.all()
    serializer_class = CompanyReminderSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["active"]


class CompanyReminderIDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company_Reminder.objects.all()
    serializer_class = CompanyReminderSerializer


class SiteReminderListView(generics.ListCreateAPIView):
    queryset = Site_Reminder.objects.all()
    serializer_class = SiteReminderSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["active"]


class SiteReminderIDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Site_Reminder.objects.all()
    serializer_class = SiteReminderSerializer
