from django.db import models
from django.utils.translation import gettext_lazy as _

# from django_countries.fields import CountryField
# Create your models here.

class Loa_Template(models.Model):
    name = models.CharField(_("Name of Template"), max_length=50)
    template = models.FileField(upload_to='LOA_templates/', )
    
    class Meta:
        verbose_name = "LOA Template"
        verbose_name_plural = "LOA Templates"


    def __str__(self):
        return self.name
class Site(models.Model):
    
    # Site Detail 
    group_name=models.CharField(max_length=128,unique=True,default="",blank=True,)
    parent_company=models.CharField(max_length=128, null=True, blank=True, verbose_name=_("Parent Company (Optional)"))
    site_name=models.CharField(max_length=128)
    company=models.ForeignKey('company.Company',on_delete=models.CASCADE, verbose_name="Company Name")
    type_of_owner=models.CharField(max_length=128)
    owner_name=models.CharField(max_length=128)
    current_gas_and_electricity_supplier_details=models.CharField(max_length=128)
    tenant = models.BooleanField(default=True)
    vacant = models.BooleanField(default=False)
    change_of_tenancy = models.BooleanField(_("CoT"), default=False)
    customer_consent = models.BooleanField(_("Please confirm customer consent has been received to be contacted regarding the current quote"), default=False)
    # Site_address
    postcode_site=models.CharField(_("Postcode"),max_length=128, blank=True)
    addressline1_site=models.CharField(_("address line 1"),max_length=128,blank=True)
    addressline2_site=models.CharField(_("address line 2"),max_length=128,null=True,blank=True)
    addressline3_site=models.CharField(_("address line 3"),max_length=128,null=True,blank=True)
    addressline4_site=models.CharField(_("address line 4"),max_length=128,null=True,blank=True)
    country_site=models.CharField(_("Country"),max_length=128, blank=True) #dropdown

    # Billing_address
    postcode_billing=models.CharField(_("Postcode"),max_length=128, blank=True)
    addressline1_billing=models.CharField(_("addressline 1"),max_length=128, blank=True)
    addressline2_billing=models.CharField(_("addressline 2"),max_length=128,null=True,blank=True)
    addressline3_billing=models.CharField(_("addressline 3"),max_length=128,null=True,blank=True)
    addressline4_billing=models.CharField(_("addressline 4"),max_length=128,null=True,blank=True)
    country_billing=models.CharField(_("Country"),max_length=128, blank=True) #

    # Our_detail
    class lead_type_choices(models.TextChoices):
        GAS='GAS',('GAS')
        ELECTRICITY='ELECTRICITY',('ELECTRICITY')      
        
    site_reference=models.CharField(max_length=128, blank=True)
    support_contact=models.ForeignKey('auth.User',on_delete=models.SET_NULL,null=True, blank=True) 
    lead_source=models.CharField(max_length=128, blank=True, null=True)
    notes=models.CharField(max_length=128, blank=True, null=True)
    
        
    lead_type = models.CharField(max_length=128,choices=lead_type_choices.choices,default=lead_type_choices.GAS,blank=True)
    bill_to_sent=models.BooleanField(default=False, verbose_name="Bill to Sent")
    welcome_letter_send=models.BooleanField(default=False, verbose_name="Welcome Letter Sent")

    # Letter_of_authority
    class loa_header(models.TextChoices):
        SITE_NAME = 1
        COMPANY_NAME = 2
        
    agent_email=models.EmailField(max_length=128, blank=True)
    loa_header_to_use=models.CharField(_("LOA Header to Use"),max_length=128, blank=True, choices=loa_header.choices)
    loa_template = models.ForeignKey(Loa_Template, verbose_name=_("LOA Template"), on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.site_name