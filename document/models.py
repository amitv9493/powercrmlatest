from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Document(models.Model):
    name = models.CharField(_("Document Name"), max_length=100)
    document = models.FileField(_("Upload Document"), upload_to="docs")
    description = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class General_Document(Document):
    class Meta:
        verbose_name = "General Document"


class Company_Document(Document):
    company = models.ForeignKey("company.Company", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Company Document"


class Site_Document(Document):
    site = models.ForeignKey("sites.Site", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Site Document"
