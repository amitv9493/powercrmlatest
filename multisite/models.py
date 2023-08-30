from django.db import models

# Create your models here.


class MultiSite(models.Model):
    class group_choice(models.TextChoices):
        BASIC = "BASIC", "Basic Group"
        mutisite = "MULTI", "Multi Site Group"

    group_name = models.CharField(max_length=255, null=True)
    sites = models.ManyToManyField("sites.Site")
    group_type = models.CharField(choices=group_choice.choices, max_length=50)
