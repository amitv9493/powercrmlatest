from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    ChangePasswordSerializer,
    LoginSerializer,
    PasswordResetSerializer,
    RegisterSerializer,
    ResetPasswordSerializer,
    UserProfileSerializer,
)
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from .serializers import *
from .renderers import UserRenderes
from sites.models import Site
from rest_framework.response import Response
from supply.models import Meter_detail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser

from rest_framework.filters import SearchFilter, OrderingFilter
from .paginator import CustomPagination
from rest_framework.permissions import IsAuthenticated

import requests
import os
from dotenv import load_dotenv

load_dotenv()
from amazon.auth.base import Token

token = Token()
# Create your views here.


def front(request):
    context = {}
    return render(request, "index.html", context)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class RegistrationView(APIView):
    renderer_classes = [UserRenderes]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()

            return Response(
                {"msg": "Registration successful"}, status=status.HTTP_201_CREATED
            )


class LoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get("username")
            password = serializer.data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response(
                    {"token": token, "msg": "login Successful"},
                    status=status.HTTP_200_OK,
                )
                token.user_data = user
            return Response(
                {"errors": {"Non_field_errors": ["username or password is not valid"]}},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    renderer_classes = [UserRenderes]
    permission_classes = [IsAuthenticated]

    # authentication_classes = [JWTAuthentication]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    renderer_classes = [UserRenderes]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = ChangePasswordSerializer(
            data=request.data, context={"user": request.user}
        )
        if serializer.is_valid(raise_exception=True):
            return Response({"msg": "Password changed"})

        return Response(serializer.errors)


class SendPasswordResetView(APIView):
    renderer_classes = [UserRenderes]

    def post(self, request, format=None):
        # try:
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(
                {"msg": "Password reset link is sent if it is registered"},
                status=status.HTTP_200_OK,
            )

    # except AssertionError:
    #     return Response({"error":"Not a valid data"})


class PasswordResetView(APIView):
    renderer_classes = [UserRenderes]

    def post(self, request, uid, token, format=None):
        serializer = ResetPasswordSerializer(
            data=request.data, context={"uid": uid, "token": token}
        )
        if serializer.is_valid(raise_exception=True):
            return Response(
                {"msg": "password reset successfully"}, status=status.HTTP_200_OK
            )


"""============================================================================================="""


class Company_view(generics.ListCreateAPIView):
    queryset = Company.objects.all()

    serializer_class = Company_Serializer
    pagination_class = CustomPagination


class Company_RUD_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = Company_Serializer


class AllUsers_view(generics.ListAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModel_Serializer


class meter_detail_list_view(APIView):
    def get_object(self, pk):
        try:
            instance = Meter_detail.objects.get(site=pk)
        except Meter_detail.DoesNotExist:
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                data={"msg": "No data with this site"},
            )

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = Meter_Detail_Serialzer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = Meter_Detail_Serialzer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data={"msg": "data is not valid "}
            )


class Current_supplies_list_view(APIView):
    def get_object(self, pk):
        try:
            instance = Current_supplies.objects.get(site=pk)
        except Current_supplies.DoesNotExist:
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                data={"msg": "No data with this site"},
            )

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = Current_supplies_Serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = Current_supplies_Serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data={"msg": "data is not valid "}
            )


class New_supplies_list_view(APIView):
    def get_object(self, pk):
        try:
            instance = New_supplies.objects.get(site=pk)
        except Meter_detail.DoesNotExist:
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                data={"msg": "No data with this site"},
            )

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = New_supplies_Serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = New_supplies_Serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data={"msg": "data is not valid "}
            )


"""==================================================================="""


class Notes_ListView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = Notes_Serializer


class Notes_CRUD_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = Notes_Serializer


"""===================================================================
                REMINDER VIEW


==================================================================="""


# from rest_framework
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


"""
===========================================================================

                        GENERATE QUOTE VIEWS

===========================================================================
"""


class GenerateQuoteListView(generics.ListCreateAPIView):
    serializer_class = GenerateQuoteSerializer
    queryset = Generate_Quote.objects.all()


class GenerateQuoteIDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GenerateQuoteSerializer
    queryset = Generate_Quote.objects.all()


from rest_framework.decorators import api_view

# class SupplyView(generics.RetrieveUpdateAPIView):
#     serializer_class = SupplyDetailSerializer
#     queryset = Supplies.objects.all()

#     def get_queryset(self):
#         qs = super().get_queryset()
#         pk = self.kwargs['pk']
#         # print(pk)

#         qs1 = qs.filter(
#             meter__site_id = pk,)
#             # current_supply__site_id = pk,
#             # new_supply__site_id = pk)
#         print(qs1)
#         return qs1


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


"""==========================================================================================

                                        QUOTE VIEW
                                        
=========================================================================================="""

# QUOTE SETTINGS
from quoting.models import Generate_Group_Quote, Quoting_Settings, Generate_Quote


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


# GENERAL QUOTES


class GeneralQuoteView(generics.ListCreateAPIView):
    serializer_class = GenerateQuoteSerializer
    queryset = Generate_Quote.objects.all()


class GeneralQuoteIDView(APIView):
    def get_object(self, pk):
        try:
            return Generate_Quote.objects.get(id=pk)
        except Generate_Quote.DoesNotExist:
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                data={"msg": "No content with this ID"},
            )

    def patch(self, request, pk):
        instance = self.get_object(pk=pk)
        if request.method == "PATCH":
            serializer = GenerateQuoteSerializer(instance, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        instance = self.get_object(pk=pk)
        if request.method == "GET":
            serializer = GenerateQuoteSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)


# GROUP QUOTE


class GroupQuoteView(generics.ListCreateAPIView):
    serializer_class = GroupQuoteSerializer
    queryset = Generate_Group_Quote.objects.all()


class GeneralDocumentView(ModelViewSet):
    parser_classes = [MultiPartParser]

    serializer_class = GeneralDocumentSerializer
    queryset = General_Document.objects.all()


class SiteDocumentView(ModelViewSet):
    parser_classes = [MultiPartParser]

    serializer_class = SiteDocumentSerializer
    queryset = Site_Document.objects.all()


class CompanyDocumentView(ModelViewSet):
    parser_classes = [MultiPartParser]

    serializer_class = CompanyDocumentSerializer
    queryset = Company_Document.objects.all()


class BusinessTypeView(generics.ListCreateAPIView):
    queryset = Business_type.objects.all()
    serializer_class = BusinessTypeSerializer

    pagination_class = None


from rest_framework.parsers import FileUploadParser


class LOATemplateView(generics.ListCreateAPIView):
    serializer_class = LOATemplateaSerailzer
    parser_classes = [MultiPartParser]
    queryset = Loa_Template.objects.all()

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES["template"]

        allowed_extensions = [".docx", ".txt"]
        if not any(file_obj.name.endswith(ext) for ext in allowed_extensions):
            return Response(
                {
                    "error": "Invalid doc Type. Only "
                    + (", ".join(ext for ext in allowed_extensions))
                    + " are allowed."
                },
                status=400,
            )
        return super().post(request, *args, **kwargs)


class LOATemplateIDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LOATemplateaSerailzer
    parser_classes = [MultiPartParser]
    queryset = Loa_Template.objects.all()

    def check_extension(self, file_obj_name, allowed_extensions):
        if not any([file_obj_name.endswith(ext) for ext in allowed_extensions]):
            return Response(
                {
                    "error": "Invalid doc Type. Only "
                    + (", ".join(ext for ext in allowed_extensions))
                    + " are allowed."
                },
                status=400,
            )

    def update(self, request, *args, **kwargs):
        file_obj_name = request.FILES.get("template", None)
        if file_obj_name:
            file_obj_name = file_obj_name.name
            allowed_extensions = [".docx", ".txt"]
            response = self.check_extension(file_obj_name, allowed_extensions)

            if response:
                return response

        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        file_obj_name = request.FILES.get("template", None)
        if file_obj_name:
            file_obj_name = file_obj_name.name
            allowed_extensions = [".docx", ".txt"]
            response = self.check_extension(file_obj_name, allowed_extensions)
            if response:
                return response
        return super().partial_update(request, *args, **kwargs)


"""
==============================================================================
                    PROGRES VIEW
==============================================================================

"""
from rest_framework import authentication
from rest_framework import permissions


class CurrentGasProgressView(generics.ListCreateAPIView):
    serializer_class = CurrentGasProgressSerializer
    queryset = Current_gas_progress.objects.all()
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.BasicAuthentication,
    ]

    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(completed_by=self.request.user)
        return super().perform_create(serializer)


class CurrentGasProgressIDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CurrentGasProgressSerializer
    queryset = Current_gas_progress.objects.all()


class CurrentElectricityProgressView(generics.ListCreateAPIView):
    serializer_class = CurrentElectricityProgressSerializer
    queryset = Current_electricity_progress.objects.all()


class CurrentElectricityProgressIDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CurrentElectricityProgressSerializer
    queryset = Current_electricity_progress.objects.all()


class NewGasProgressView(generics.ListCreateAPIView):
    serializer_class = NewGasProgressSerializer
    queryset = New_gas_progress.objects.all()


class NewGasProgressIDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewGasProgressSerializer
    queryset = New_gas_progress.objects.all()


class NewElectricityProgressView(generics.ListCreateAPIView):
    serializer_class = NewElectricityProgressSerializer
    queryset = New_electricity_progress.objects.all()


class NewElectricityProgressIDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewElectricityProgressSerializer
    queryset = New_electricity_progress.objects.all()


"""===================================================================================

                    SP API AUTHENTICATION

======================================================================================
"""

import requests
from django.shortcuts import redirect
from document.models import user_credentials


from rest_framework_simplejwt.authentication import JWTAuthentication

from amazon.auth.base import Token

token = Token()


class authenticate_amazon(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [authentication.BasicAuthentication]

    def get(self, request):
        url_base = f"https://sellercentral.amazon.in/apps/authorize/consent?application_id={os.getenv('LWA_APP_ID')}&state={request.user.id}&version=beta"

        return redirect(url_base)


class save_credentials(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        complete_uri = request.build_absolute_uri()
        print(complete_uri)

        data = request.query_params
        code = data.get("spapi_oauth_code")
        selling_partner_id = data.get("selling_partner_id")
        state = int(data.get("state"))

        user = get_user_model().objects.get(id=state)

        cred, _ = user_credentials.objects.get_or_create(user=user)
        cred.code = code
        cred.selling_partner_id = selling_partner_id
        cred.save()

        get_token(user=user, grant_type="authorization_code", request=None)

        return Response({"msg": "success"}, status=200)


def get_token(user, grant_type, request=None):
    url = "https://api.amazon.com/auth/o2/token"

    user_data = user_credentials.objects.get(user=user)

    if grant_type == "authorization_code":
        token = user_data.code
        type = "code"
    elif grant_type == "refresh_token":
        token = user_data.refresh_token
        type = "refresh_token"

    payload = f"grant_type={grant_type}&{type}={token}&client_id={os.getenv('client_id')}&client_secret={os.getenv('client_secret')}"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(url, headers=headers, data=payload)

    token_data = response.json()
    print(token_data)

    if token_data.get("error"):
        return Response(token_data, status=400)

    user_data.access_token = token_data.get("access_token")
    user_data.refresh_token = token_data.get("refresh_token")

    user_data.save()


def set_session_token(request, user_data):
    request.session["access_token"] = user_data.access_token




class Orders(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [
        # JWTAuthentication,
        authentication.BasicAuthentication,
        authentication.SessionAuthentication,
    ]

    def get(self, request, format=None):
        data = user_credentials.objects.filter(user=request.user).first()
        token.user_data = data
        print(token.access_token)
        created_after = request.query_params.get("created_after", None)
        url = f"https://sellingpartnerapi-eu.amazon.com/orders/v0/orders?MarketplaceIds={data.market_place_id}&CreatedAfter={created_after}"
        sandbox_url = f"https://sandbox.sellingpartnerapi-eu.amazon.com/orders/v0/orders?MarketplaceIds={data.market_place_id}&CreatedAfter=TEST_CASE_200"

        def get_orders():
            payload = {}

            headers = {
                "x-amz-access-token": token.access_token,
            }
            response = requests.get(sandbox_url, headers=headers, data=payload)
            return response

        response = get_orders()
        if 400 <= response.status_code <= 499:
            # get_token(request=request, user=request.user, grant_type="refresh_token")
            token.GenerateAccessToken(grant_type="refresh_token")
            print(token.access_token)

            response = get_orders()
        elif response.status_code >=500:
            return Response({"error": "Internal Server occured"}, status=500)
        print(response)
        print(response.status_code)
        return Response(response.json(), status=200)


class hello(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.a]
    
    def post(self, request):
        
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get("username")
            password = serializer.data.get("password")
            
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                
            return Response({"msg":"logged In successfully"},status=200)