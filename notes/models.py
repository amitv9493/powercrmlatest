from django.db import models
# Create your models here.

class Note(models.Model):
    select_site = models.OneToOneField("sites.Site",verbose_name=('Selected Site'), on_delete=models.CASCADE)
    site_notes=models.TextField(null=True, blank=True)
    company_notes=models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.select_site.__str__