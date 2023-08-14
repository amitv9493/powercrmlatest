from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Business_type(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Business type"
        verbose_name = "Business type"


class Company(models.Model):
    # Company Info
    name = models.CharField(_("Name of the Company"), max_length=100)
    number_of_employees = models.PositiveIntegerField()
    registration_no = models.CharField(max_length=128)
    business_type = models.ForeignKey(
        Business_type,
        verbose_name=_("Company Type"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    estimated_turnover = models.IntegerField()
    is_macro_business = models.BooleanField(_("Is Micro Business?"), default=False)
    credit_score = models.IntegerField(_("Credit Score"), null=True, blank=True)
    sic_code = models.CharField(_("SIC Code "), max_length=50, null=True, blank=True)

    # Company address
    addressline1_company = models.CharField(
        _("Address Line 1 "), max_length=50, null=True, blank=True
    )
    addressline2_company = models.CharField(
        _("Address Line 2 "), max_length=50, null=True, blank=True
    )
    addressline3_company = models.CharField(
        _("Address Line 3 "), max_length=50, null=True, blank=True
    )
    postcode = models.IntegerField(_("Postcode"), null=True, blank=True)
    country_of_company = models.CharField(
        _("Country"), max_length=50, null=True, blank=True
    )

    # Bank Details
    account_name = models.CharField(max_length=128)
    bank_name = models.CharField(max_length=128)
    account_no = models.CharField(max_length=128)
    shortcode = models.CharField(max_length=128)

    # Partner Details
    partner_name = models.CharField(max_length=128, blank=True)
    home_post_code = models.CharField(max_length=128, blank=True)
    partner_dob = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    time_at_address_years = models.PositiveIntegerField(
        verbose_name="Time At Address(years)", blank=True, null=True
    )
    time_at_address_months = models.PositiveIntegerField(
        verbose_name="Time At Address(months)", blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"
        verbose_name = "Company"
