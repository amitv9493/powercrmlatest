from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Current_supplies, New_supplies


@receiver(post_save, sender=New_supplies)
def create_new_supply_usage_rats(sender, instance, created, **kwargs):
    if created:
        instance.usage_rates.create(usage_type="GAS")
        instance.usage_rates.create(usage_type="ELECTRIC")


@receiver(post_save, sender=Current_supplies)
def create_current_supply_usage_rats(sender, instance, created, **kwargs):
    if created:
        instance.usage_rates.create(usage_type="GAS")
        instance.usage_rates.create(usage_type="ELECTRIC")
