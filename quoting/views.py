from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from multisite.models import MultiSite

from .models import Generate_Group_Quote, Generate_Quote, Quoting_Settings
from .serializers import (
    GenerateQuoteSerializer,
    GroupQuoteGETSerializer,
    GroupQuotePOSTSerializer,
    Multisite_QuotingSerializer,
    QuoteSettingSerializer,
)

# Create your views here.


# GENERAL QUOTES
class GenerateQuoteView(generics.ListCreateAPIView):
    serializer_class = GenerateQuoteSerializer
    queryset = Generate_Quote.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["site"]


class GenerateQuoteIDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GenerateQuoteSerializer
    queryset = Generate_Quote.objects.all()


# QUOTE SETTINGS
@api_view(["GET"])
def QuoteSettingView(request):
    if request.method == "GET":
        queryset = Quoting_Settings.objects.all()
        serializer = QuoteSettingSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(["PUT"])
def QuoteSettingInstanceView(request, pk):
    try:
        instance = Quoting_Settings.objects.get(id=pk)
    except Quoting_Settings.DoesNotExist:
        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data={"msg": "No settting with this ID please provide `pk=1`"},
        )

    if request.method == "PUT":
        serializer = QuoteSettingSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data={"msg": "Not a valid data"}
            )


# GROUP QUOTE
class GroupQuoteView(ModelViewSet):
    serializer_class = GroupQuoteGETSerializer
    queryset = Generate_Group_Quote.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return GroupQuotePOSTSerializer
        return super().get_serializer_class()


@api_view(["GET"])
@permission_classes([])
def recent_quotes(request):
    queryset = Generate_Quote.objects.all().order_by("-date_created")[:10]

    return Response(GenerateQuoteSerializer(queryset, many=True).data)


class Multisite_Quoting(APIView):
    queryset = MultiSite.objects.all()

    def get_object(self, pk):
        try:
            return MultiSite.objects.get(pk=pk)
        except MultiSite.DoesNotExist:
            return None

    def post(self, request, pk):
        multisite_object = self.get_object(pk)

        if multisite_object is not None:
            serializer = Multisite_QuotingSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                for i in multisite_object.sites.all():
                    quote_instance, created = Generate_Quote.objects.get_or_create(
                        site=i
                    )
                    for key, value in serializer.validated_data.items():
                        setattr(quote_instance, key, value)

                    quote_instance.save(update_fields=serializer.validated_data.keys())
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(
                "no multisite with this ID", status=status.HTTP_400_BAD_REQUEST
            )
