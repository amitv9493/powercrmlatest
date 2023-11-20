from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.decorators import api_view

# Create your views here.

class meter_detail_list_view(APIView):

        
    def get(self, request, pk, format=None):
        try:
            instance = Meter_detail.objects.get(site=pk)
            
        except Meter_detail.DoesNotExist:
            return Response({"error":"Object with this site ID does not exists"}, status.HTTP_400_BAD_REQUEST)
        
        serializer = Meter_Detail_Serialzer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        try:
            instance = Meter_detail.objects.get(site=pk)
            
        except Meter_detail.DoesNotExist:
            return Response({"error":"Object with this site ID does not exists"},status.HTTP_400_BAD_REQUEST )
        
        serializer = Meter_Detail_Serialzer(instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
class Current_supplies_list_view(APIView):

    def get(self, request, pk, format=None):
        try:
            instance = Current_supplies.objects.get(site=pk)
        except Current_supplies.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST,data={"msg": "No data with this site"},
            )

        serializer = Current_supplies_Serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        try:
            instance = Current_supplies.objects.get(site=pk)
            
        except Current_supplies.DoesNotExist:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"msg": "No data with this site"},
            )

        serializer = Current_supplies_Serializer(instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)




class New_supplies_list_view(APIView):

    def get(self, request, pk, format=None):
        try:
            instance = New_supplies.objects.get(site=pk)
            
        except New_supplies.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST,data={"msg": "No data with this site"},)
            
        serializer = New_supplies_Serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        try:
            instance = New_supplies.objects.get(site=pk)
        except New_supplies.DoesNotExist:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"msg": "No data with this site"},
            )
            
        serializer = New_supplies_Serializer(instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "PATCH", "PUT"])
def SupplyView(request, site_id):
    try:
        instance = Supplies.objects.get(
            meter__site_id=site_id,
            current_supply__site_id=site_id,
            new_supply__site_id=site_id,
        )

    except Supplies.DoesNotExist:
        return Response(
            status=status.HTTP_204_NO_CONTENT, data={"msg": "No data for this site"}
        )

    if request.method == "GET":
        serializer = SupplyDetailSerializer(instance)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = SupplyDetailSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

