from django.dispatch import receiver
from django.db.models.signals import post_save

from supply.models import Supplies
from .models import Site, SiteAddress, BillingAddress
from supply.models import Meter_detail, New_supplies, Current_supplies
from contacts.models import Contacts


@receiver(post_save, sender=Site)
def Create_Related_Objects(sender, instance, created, **kwargs):
    if created:
        meter_detail = Meter_detail.objects.create(site=instance)
        new_supply = New_supplies.objects.create(site=instance)
        current_supply = Current_supplies.objects.create(site=instance)

        SiteAddress.objects.create(site=instance)
        BillingAddress.objects.create(site=instance)
        Contacts.objects.create(site=instance)

        supply = Supplies()
        supply.meter = meter_detail
        supply.current_supply = current_supply
        supply.new_supply = new_supply
        supply.save()
