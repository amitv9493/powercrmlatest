from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Current_gas_progress(models.Model):
    action = models.CharField(max_length=128)
    completed = models.BooleanField(default=False)

    class priorityTextChoices(models.TextChoices):
        LOW = "LOW", ("Low")
        MODERATE = "MODERATE", ("Moderate")
        CRITICAL = "CRITICAL", ("Critical")

    priority = models.CharField(
        max_length=128,
        choices=priorityTextChoices.choices,
        default=priorityTextChoices.LOW,
    )
    set_status_to = models.CharField(max_length=128)
    completed_by = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True, blank=True
    )
    callback = models.BooleanField(default=False)

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = "Current gas progress"
        verbose_name_plural = "Current gas progresses"


class Current_electricity_progress(models.Model):
    action = models.CharField(max_length=128)
    completed = models.BooleanField(default=False)

    class priorityTextChoices(models.TextChoices):
        LOW = "LOW", ("Low")
        MODERATE = "MODERATE", ("Moderate")
        CRITICAL = "CRITICAL", ("Critical")

    priority = models.CharField(
        max_length=128,
        choices=priorityTextChoices.choices,
        default=priorityTextChoices.LOW,
    )
    completed_by = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True, blank=True
    )
    set_status_to = models.CharField(max_length=128)
    callback = models.BooleanField(default=False)

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = "Current electricity progress"
        verbose_name_plural = "Current electricity progress"


class New_gas_progress(models.Model):
    action = models.CharField(max_length=128)
    completed = models.DateTimeField(auto_now=False, auto_now_add=True)

    class priorityTextChoices(models.TextChoices):
        LOW = "LOW", ("Low")
        MODERATE = "MODERATE", ("Moderate")
        CRITICAL = "CRITICAL", ("Critical")

    priority = models.CharField(
        max_length=128,
        choices=priorityTextChoices.choices,
        default=priorityTextChoices.LOW,
    )
    completed_by = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True, blank=True
    )
    set_status_to = models.CharField(max_length=128)

    callback = models.BooleanField(default=False)

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = "New gas progress"
        verbose_name_plural = "New gas progress"


class New_electricity_progress(models.Model):
    action = models.CharField(max_length=128)
    completed = models.DateTimeField(auto_now=False, auto_now_add=True)

    class priorityTextChoices(models.TextChoices):
        LOW = "LOW", ("Low")
        MODERATE = "MODERATE", ("Moderate")
        CRITICAL = "CRITICAL", ("Critical")

    priority = models.CharField(
        max_length=128,
        choices=priorityTextChoices.choices,
        default=priorityTextChoices.LOW,
    )
    set_status_to = models.CharField(max_length=128)
    completed_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        # null=True,
    )
    callback = models.BooleanField(default=False)

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = "New electricity progress"
        verbose_name_plural = "New electricity progress"
