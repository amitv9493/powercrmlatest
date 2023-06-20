from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class General_Document(models.Model):
    document =  models.FileField(_("Upload Document"), upload_to="general_docs")
    name = models.CharField(_("Document Name"), max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "General Document"

class Company_Document(models.Model):
    company = models.ForeignKey("company.Company", on_delete=models.CASCADE)
    document =  models.FileField(_("Upload Document"), upload_to="company_docs")
    name = models.CharField(_("Document Name"), max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Company Document"

class Site_Document(models.Model):
    name = models.CharField(_("Document Name"), max_length=100)
    site = models.ForeignKey("sites.Site", on_delete=models.CASCADE)
    document =  models.FileField(_("Upload Document"), upload_to="site_docs")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Site Document"
