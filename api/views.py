import json
from typing import Dict, Optional

import requests
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import render
from dotenv import load_dotenv
from rest_framework import authentication, generics, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from amazon.auth.base import Token
from company.models import Business_type, Company
from document.models import Company_Document, General_Document, Site_Document
from notes.models import Note
from progress.models import (
    Current_electricity_progress,
    Current_gas_progress,
    New_electricity_progress,
    New_gas_progress,
)
from sites.models import Loa_Template

from .paginator import CustomPagination
from .renderers import UserRenderes
from .serializers import (
    BusinessTypeSerializer,
    ChangePasswordSerializer,
    Company_Serializer,
    CompanyDocumentSerializer,
    CurrentElectricityProgressSerializer,
    CurrentGasProgressSerializer,
    GeneralDocumentSerializer,
    LOATemplateaSerailzer,
    LoginSerializer,
    NewElectricityProgressSerializer,
    NewGasProgressSerializer,
    Notes_Serializer,
    PasswordResetSerializer,
    RegisterSerializer,
    ResetPasswordSerializer,
    SiteDocumentSerializer,
    UserModel_Serializer,
    UserProfileSerializer,
)

load_dotenv()

token = Token()
User = get_user_model()
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
            serializer.save()

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

# import requests
# from django.shortcuts import redirect
# from document.models import user_credentials


# from amazon.auth.base import Token

# token = Token()


# class authenticate_amazon(APIView):
#     permission_classes = [
#         IsAuthenticated,
#     ]
#     authentication_classes = [authentication.BasicAuthentication]

#     def get(self, request):
#         url_base = f"https://sellercentral.amazon.in/apps/authorize/consent?application_id={os.getenv('LWA_APP_ID')}&state={request.user.id}&version=beta"

#         return redirect(url_base)


# class save_credentials(APIView):
#     permission_classes = []
#     authentication_classes = []

#     def get(self, request):
#         complete_uri = request.build_absolute_uri()
#         print(complete_uri)

#         data = request.query_params
#         code = data.get("spapi_oauth_code")
#         selling_partner_id = data.get("selling_partner_id")
#         state = int(data.get("state"))

#         user = get_user_model().objects.get(id=state)

#         cred, _ = user_credentials.objects.get_or_create(user=user)
#         cred.code = code
#         cred.selling_partner_id = selling_partner_id
#         cred.save()

#         get_token(user=user, grant_type="authorization_code", request=None)

#         return Response({"msg": "success"}, status=200)


# def get_token(user, grant_type, request=None):
#     url = "https://api.amazon.com/auth/o2/token"

#     user_data = user_credentials.objects.get(user=user)

#     if grant_type == "authorization_code":
#         token = user_data.code
#         type = "code"
#     elif grant_type == "refresh_token":
#         token = user_data.refresh_token
#         type = "refresh_token"

#     payload = f"grant_type={grant_type}&{type}={token}&client_id={os.getenv('client_id')}&client_secret={os.getenv('client_secret')}"
#     headers = {"Content-Type": "application/x-www-form-urlencoded"}

#     response = requests.post(url, headers=headers, data=payload)

#     token_data = response.json()
#     print(token_data)

#     if token_data.get("error"):
#         return Response(token_data, status=400)

#     user_data.access_token = token_data.get("access_token")
#     user_data.refresh_token = token_data.get("refresh_token")

#     user_data.save()


# def set_session_token(request, user_data):
#     request.session["access_token"] = user_data.access_token


# class Orders(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = [
#         # JWTAuthentication,
#         authentication.BasicAuthentication,
#         authentication.SessionAuthentication,
#     ]

#     def get(self, request, format=None):
#         data = user_credentials.objects.filter(user=request.user).first()
#         token.user_data = data
#         print(token.access_token)
#         created_after = request.query_params.get("created_after", None)
#         url = f"https://sellingpartnerapi-eu.amazon.com/orders/v0/orders?MarketplaceIds={data.market_place_id}&CreatedAfter={created_after}"
#         sandbox_url = f"https://sandbox.sellingpartnerapi-eu.amazon.com/orders/v0/orders?MarketplaceIds={data.market_place_id}&CreatedAfter=TEST_CASE_200"

#         def get_orders():
#             payload = {}

#             headers = {
#                 "x-amz-access-token": token.access_token,
#             }
#             response = requests.get(sandbox_url, headers=headers, data=payload)
#             return response

#         response = get_orders()
#         if 400 <= response.status_code <= 499:
#             # get_token(request=request, user=request.user, grant_type="refresh_token")
#             token.GenerateAccessToken(grant_type="refresh_token")
#             print(token.access_token)

#             response = get_orders()
#         elif response.status_code >=500:
#             return Response({"error": "Internal Server occured"}, status=500)
#         print(response)
#         print(response.status_code)
#         return Response(response.json(), status=200)


class LookupViewset(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    lookup_url = "https://api.lookup.energy"

    def get_headers(self, request):
        try:
            headers = request.data.get("headers", None)
            return headers
        except Exception:
            return None

    def get_token(self, request):
        url = f"{self.lookup_url}/api/Auth/GetBearer"

        payload = json.dumps(
            {"username": settings.LOOKUP_EMAIL, "password": settings.LOOKUP_PASSWORD}
        )

        headers = {
            "content-type": "application/json",
            "accept": "application/json",
        }

        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200:
            request.session["lookupToken"] = response.json()["value"]["bearerToken"]
            # return data.json()["value"]["bearerToken"]
        else:
            return Response(response.content, status=response.status_code)

    def common_pattern(self, request, url: str, header: Optional[Dict] = None):
        if request.session.get("lookupToken", None) is None:
            self.get_token(request)

        url = f"{self.lookup_url}/{url}"
        print("requesting url", url)

        def get_details():
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {request.session.get('lookupToken')}",
            }
            if header:
                headers.update(header)
            payload = json.dumps(request.data)
            return requests.post(url, headers=headers, data=payload)

        response = get_details()

        if response.status_code == 401:
            self.get_token(request)
            response = get_details()

        if response.status_code == 200:
            return Response(response.json(), status=response.status_code)
        else:
            return Response(response.content, status=response.status_code)

    @action(detail=False, methods=["POST"], url_path="Electricity/SearchBypMpan")
    def electrycity_search(self, request):
        headers = self.get_headers(request)
        response = self.common_pattern(request, "api/Electricity/SearchByMpan", headers)

        return response

    def list(self, request):
        headers = self.get_headers(request)

        response = self.common_pattern(
            request,
            "api/Usage/GetMySummary",
            headers,
        )
        return response

    @action(detail=False, methods=["POST"], url_path="Electricity/ValidateMpan")
    def validate_MPAN(self, request):
        headers = self.get_headers(request)
        response = self.common_pattern(
            request,
            "api/Electricity/ValidateMpan",
            headers,
        )
        return response

    @action(detail=False, methods=["POST"], url_path="Property/SearchByPostcode")
    def SearchByPostcode(self, request):
        headers = self.get_headers(request)
        response = self.common_pattern(
            request, "api/Property/SearchByPostcode", headers
        )
        return response
