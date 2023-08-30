from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from company.models import *
from contacts.models import Contacts
from document.models import General_Document
from sites.models import Loa_Template, Site
from drf_writable_nested.serializers import WritableNestedModelSerializer
from supply.models import *
from notes.models import Note
from reminder.models import Company_Reminder, Site_Reminder, General_Reminder
from document.models import Company_Document, Site_Document
from django.contrib.auth import get_user_model
from drf_writable_nested.serializers import WritableNestedModelSerializer

User = get_user_model()
#


class UserModel_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


from contacts.serializers import ContactSerializer


class Company_Serializer(serializers.ModelSerializer):
    contacts = ContactSerializer(required=False)

    class Meta:
        model = Company
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        contacts = validated_data.pop("contacts", None)
        x = super().create(validated_data)

        if contacts:
            Contacts.objects.create(company=x, **contacts)
        return x


# ====================================================================


class Meter_Detail_Serialzer(serializers.ModelSerializer):
    class Meta:
        model = Meter_detail
        fields = "__all__"


class Current_supplies_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Current_supplies
        fields = "__all__"


class New_supplies_Serializer(serializers.ModelSerializer):
    class Meta:
        model = New_supplies
        fields = "__all__"


class Notes_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"


class CompanyReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_Reminder
        fields = "__all__"


class SiteReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site_Reminder
        fields = "__all__"


class GeneralReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = General_Reminder
        fields = "__all__"


# ============================================================================================

# ============================================================================================


class SupplyDetailSerializer(WritableNestedModelSerializer):
    meter = Meter_Detail_Serialzer()
    current_supply = Current_supplies_Serializer()
    new_supply = New_supplies_Serializer()

    class Meta:
        model = Supplies
        fields = "__all__"


"""
==================================================================================

                            DOCUMENT VIEWS

===================================================================================

"""


class GeneralDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = General_Document
        fields = "__all__"


class SiteDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site_Document
        fields = "__all__"


class CompanyDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_Document
        fields = "__all__"


class BusinessTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business_type
        fields = "__all__"


class LOATemplateaSerailzer(serializers.ModelSerializer):
    class Meta:
        model = Loa_Template
        fields = "__all__"


"""
===========================================================================================

                                PROGRESS SERIALIZERS

===========================================================================================

"""
from progress.models import *


class CurrentGasProgressSerializer(serializers.ModelSerializer):
    completed_by = serializers.PrimaryKeyRelatedField(read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        completed_by = instance.completed_by
        if completed_by is not None:
            data["completed_by"] = completed_by.username
        return data

    class Meta:
        model = Current_gas_progress
        fields = "__all__"
        # extra_kwargs = {"completed_by": {"write_only": False}}


class CurrentElectricityProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Current_electricity_progress
        fields = "__all__"

    completed_by = serializers.PrimaryKeyRelatedField(read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        completed_by = instance.completed_by
        if completed_by is not None:
            data["completed_by"] = completed_by.username
        return data


class NewGasProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = New_gas_progress
        fields = "__all__"

    completed_by = serializers.PrimaryKeyRelatedField(read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        completed_by = instance.completed_by
        if completed_by is not None:
            data["completed_by"] = completed_by.username
        return data


class NewElectricityProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = New_electricity_progress
        fields = "__all__"

    completed_by = serializers.PrimaryKeyRelatedField(read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        completed_by = instance.completed_by
        if completed_by is not None:
            data["completed_by"] = completed_by.username
        return data


"""
============================================================================================
                        ************** USER REGISTRATION SERIALIZERS ****************

============================================================================================


"""


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email"]


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ["username", "password"]


class ChangePasswordSerializer(serializers.ModelSerializer):
    current_password = serializers.CharField(
        max_length=55, style={"input_type": "password"}, write_only=True
    )
    password = serializers.CharField(
        max_length=55,
        style={"input_type": "password"},
        validators=[validate_password],
        write_only=True,
    )
    password2 = serializers.CharField(
        max_length=55, style={"input_type": "password"}, write_only=True
    )

    class Meta:
        model = User
        fields = ["current_password", "password", "password2"]

    def validate(self, attrs):
        password = attrs["password"]
        password2 = attrs["password2"]
        user = self.context.get("user")
        success = user.check_password(attrs["current_password"])

        if password == password2 and success:
            user.set_password(password)
            user.save()
            return attrs
        raise serializers.ValidationError("password do not match")


"""See imported modules carefully for reset view"""
from . import utils
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class PasswordResetSerializer(serializers.Serializer):
    email_id = serializers.EmailField()

    class Meta:
        fields = ["email_id"]

    def validate(self, attrs):
        email = attrs["email_id"]
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print(uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print(token)
            link = "http://localhost:8000/api/user/resetpassword/" + uid + "/" + token
            print(link)
            # send email
            data = {
                "subject": "Reset Your Password",
                "body": "Click on the below link to reset your password \n" + link,
                "to_email": [user.email],
            }
            utils.send_email(data)  # type: ignore
            return attrs
        raise serializers.ValidationError("This email is not registered!")


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=55,
        style={"input_type": "password"},
        validators=[validate_password],
        write_only=True,
    )
    password2 = serializers.CharField(
        max_length=55, style={"input_type": "password"}, write_only=True
    )

    class Meta:
        fields = ["password", "password2"]

    def validate(self, attrs):
        password = attrs["password"]
        password2 = attrs["password2"]
        uid = self.context.get("uid")
        token = self.context.get("token")
        print(token)
        id = smart_str(urlsafe_base64_decode(uid))  # type: ignore
        user = User.objects.get(id=id)

        # try:
        #     if not PasswordResetTokenGenerator().check_token(user, token):
        #         raise serializers.ValidationError("Link is expired or already used!")

        #     if password == password2:
        #         user.set_password(password)
        #         user.save()
        #         return attrs
        #     raise serializers.ValidationError("password do not match")

        # except DjangoUnicodeDecodeError as identifier:
        #     PasswordResetTokenGenerator().check_token(user,token)
        try:
            if PasswordResetTokenGenerator().check_token(user, token):
                print("token is correct")
                if password == password2:
                    user.set_password(password)
                    user.save()
                    return attrs
                raise serializers.ValidationError("password do not match")

            raise serializers.ValidationError("Link is expired or already used!")

        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise serializers.ValidationError("Token is not valid or expired.")
