from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class General_Document(models.Model):
    document = models.FileField(_("Upload Document"), upload_to="general_docs")
    name = models.CharField(_("Document Name"), max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "General Document"


class Company_Document(models.Model):
    company = models.ForeignKey("company.Company", on_delete=models.CASCADE)
    document = models.FileField(_("Upload Document"), upload_to="company_docs")
    name = models.CharField(_("Document Name"), max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company Document"


class Site_Document(models.Model):
    name = models.CharField(_("Document Name"), max_length=100)
    site = models.ForeignKey("sites.Site", on_delete=models.CASCADE)
    document = models.FileField(_("Upload Document"), upload_to="site_docs")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Site Document"


from django.contrib.auth import get_user_model
from django.conf import settings


class user_credentials(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(max_length=255, null=True)
    selling_partner_id = models.CharField(max_length=255, null=True)

    access_token = models.TextField(null=True)
    refresh_token = models.TextField(null=True)

    def __str__(self):
        return str(self.user.username)
