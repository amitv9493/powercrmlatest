from django.db import models

# Create your models here.


class Generate_Quote(models.Model):
    site = models.ForeignKey("sites.Site", on_delete=models.CASCADE)
    supplier = models.CharField(max_length=128, default="")
    product = models.CharField(max_length=128, default="")
    term = models.IntegerField(null=True)
    day_rate = models.FloatField(verbose_name="Day Rate(pence/kwh)", null=True)
    night_rate = models.FloatField(verbose_name="Night Rate(pence/kwh)", null=True)
    # class standing_charge(models.TextChoices):
    #     perday='perday',('perday')
    #     permonth='permonth',('permonth')
    #     peryear='peryear',('peryear')
    standing_charge = models.FloatField(
        verbose_name="Standing Charge(pence)", max_length=128, null=True
    )
    # class kva_charge(models.TextChoices):
    #     perday='perday',('perday')
    #     permonth='permonth',('permonth')
    kva_charge = models.FloatField(
        verbose_name="KVA Charge(pence)", max_length=128, null=True
    )
    additional_charge = models.FloatField(
        verbose_name="Additional Charge(£)",
        null=True,
        blank=True,
    )
    extra_info = models.CharField(max_length=128, default="", null=True, blank=True)
    up_lift = models.FloatField(verbose_name="Up Lift", null=True)
    rates_already_include_at_uplift = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.site}-{self.supplier}"

    class Meta:
        verbose_name = "Generate Quote"
        verbose_name_plural = "Generate Quotes"


class Generate_Group_Quote(models.Model):
    group_name = models.CharField(blank=True, null=True, max_length=50)
    group_detail = models.ManyToManyField("Generate_Quote")

    class Meta:
        verbose_name = "Generate Group Quote"
        verbose_name_plural = "Generate Group Quotes"


class Quoting_Settings(models.Model):
    allow_custom_contract_end_date = models.BooleanField(
        default=False, verbose_name="Allow Custom Contract End Date"
    )
    include_feed_in_tariff_charges_in_prices = models.BooleanField(
        default=False, verbose_name="Include Feed-in Tariff(FiT) charges in prices"
    )

    class Meta:
        verbose_name = "Quoting Setting"
        verbose_name_plural = "Quoting Settings"
