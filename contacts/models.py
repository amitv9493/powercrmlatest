from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Contacts(models.Model):
    # Contact Details
    class contact_titles(models.TextChoices):
        Sir = "Sir", ("Sir")
        Mr = "Mr", ("Mr")
        Ms = "Ms", ("Ms")
        Mrs = "Mrs", ("Mrs")
        Miss = "Miss", ("Miss")
        Dr = "Dr", ("Dr")
        pass

    company = models.OneToOneField(
        "company.Company",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="contacts",
    )
    site = models.OneToOneField(
        "sites.Site",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="contacts",
    )
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    contact_title = models.CharField(max_length=128, choices=contact_titles.choices)
    position = models.CharField(max_length=128)
    telephone_number = models.CharField(max_length=14)
    email = models.EmailField(max_length=128)

    @property
    def get_full_name(self):
        return f"{self.contact_title} {self.first_name} {self.last_name}"

    # def __str__(self):
    #     return self.get_full_name

    class Meta:
        verbose_name_plural = "Contacts"
