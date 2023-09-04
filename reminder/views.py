from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, status 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
# Create your views here.

class GeneralReminderListView(generics.ListCreateAPIView):
    queryset = General_Reminder.objects.all()
    serializer_class = GeneralReminderSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["active"]


class GeneralReminderIDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = General_Reminder.objects.all()
    serializer_class = GeneralReminderSerializer

    # def get_object(self, pk):

    def retrieve(self, request, pk):
        try:
            instance = General_Reminder.objects.get(id=pk)

        except General_Reminder.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

        return super().retrieve(request, pk)


class CompanyReminderListView(generics.ListCreateAPIView):
    queryset = Company_Reminder.objects.all()
    serializer_class = CompanyReminderSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["active"]


class CompanyReminderIDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company_Reminder.objects.all()

    def retrieve(self, request, pk):
        try:
            instance = Company_Reminder.objects.get(id=pk)

        except Company_Reminder.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

        return super().retrieve(request, pk)

    serializer_class = CompanyReminderSerializer


class SiteReminderListView(generics.ListCreateAPIView):
    queryset = Site_Reminder.objects.all()
    serializer_class = SiteReminderSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["active"]


class SiteReminderIDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Site_Reminder.objects.all()
    serializer_class = SiteReminderSerializer

    def retrieve(self, request, pk):
        try:
            instance = Site_Reminder.objects.get(id=pk)

        except Site_Reminder.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

        return super().retrieve(request, pk)
    