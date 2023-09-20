from rest_framework import generics, status
from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes

# Create your views here.


# GENERAL QUOTES
class GenerateQuoteView(generics.ListCreateAPIView):
    serializer_class = GenerateQuoteSerializer
    queryset = Generate_Quote.objects.all()


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
class GroupQuoteView(generics.ListCreateAPIView):
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
