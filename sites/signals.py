from django.dispatch import receiver
from django.db.models.signals import post_save

from supply.models import Supplies
from .models import Site
from supply.models import Meter_detail, New_supplies, Current_supplies

@receiver(post_save, sender=Site)
def Create_Meter_Detail(sender, instance,created, **kwargs):
    if created:
        Meter_detail.objects.create(site = instance)
        
@receiver(post_save, sender=Site)
def Create_New_Supply(sender, instance, created, **kwargs):
    if created:
        New_supplies.objects.create(site=instance)

        
@receiver(post_save, sender=Site)
def Create_Current_Supply(sender, instance, created, **kwargs):
    if created:
        Current_supplies.objects.create(site=instance)
        
        
@receiver(post_save, sender=Site)
def Create_Supplies(sender, instance, created,**kwargs):
    if created:
        supply  = Supplies()
        supply.meter = Meter_detail.objects.get(site = instance)
        supply.current_supply = Current_supplies.objects.get(site= instance)
        supply.new_supply = New_supplies.objects.get(site= instance)
        supply.save()