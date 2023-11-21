from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class General_Reminder(models.Model):
    alert = models.DateTimeField(_("Alert Date and Time "), null=True, blank=True)
    priority = models.IntegerField()

    class reminder(models.TextChoices):
        Callback = "Callback", ("Callback")
        Quotecallback = "Quotecallback", ("Quote callback")
        Fsocallback = "Fsocallback", ("Fsocallback")
        Renewalcallback = "Renewalcallback", ("Renewal callback")
        Other = "Other", ("Other")

    reminder_type = models.CharField(max_length=128, choices=reminder.choices)
    active = models.BooleanField(_("Active"), default=True)

    def __str__(self):
        return self.reminder_type

    class Meta:
        verbose_name = "General Reminder"
        verbose_name_plural = "General Reminders"


class Company_Reminder(models.Model):
    company = models.ForeignKey(
        "company.Company", verbose_name=_("Select Company"), on_delete=models.CASCADE
    )
    alert = models.DateTimeField(
        _("Alert Date and Time "),
        null=True,
        blank=True,
    )
    priority = models.IntegerField()

    class reminder(models.TextChoices):
        Callback = "Callback", ("Callback")
        Quotecallback = "Quotecallback", ("Quote callback")
        Fsocallback = "Fsocallback", ("Fsocallback")
        Renewalcallback = "Renewalcallback", ("Renewal callback")
        Other = "Other", ("Other")

    reminder_type = models.CharField(max_length=128, choices=reminder.choices)
    active = models.BooleanField(_("Active"), default=True)

    def __str__(self):
        return self.reminder_type

    class Meta:
        verbose_name = "Company Reminder"
        verbose_name_plural = "Company Reminders"


class Site_Reminder(models.Model):
    site = models.ForeignKey(
        "sites.Site", verbose_name=_("Select Site"), on_delete=models.CASCADE
    )
    alert = models.DateTimeField(
        _("Alert Date and Time "),
        null=True,
        blank=True,
    )
    priority = models.IntegerField()

    class reminder(models.TextChoices):
        Callback = "Callback", ("Callback")
        Quotecallback = "Quotecallback", ("Quote callback")
        Fsocallback = "Fsocallback", ("Fsocallback")
        Renewalcallback = "Renewalcallback", ("Renewal callback")
        Other = "Other", ("Other")

    reminder_type = models.CharField(max_length=128, choices=reminder.choices)
    active = models.BooleanField(_("Active"), default=True)

    def __str__(self):
        return self.reminder_type

    class Meta:
        verbose_name = "Site Reminder"
        verbose_name_plural = "Site Reminders"
