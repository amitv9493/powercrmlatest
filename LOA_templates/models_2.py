from django.db import models
from django.contrib.auth.models import User

# from pytz import timezone
from django.urls import reverse
from django.core.exceptions import ValidationError

# Create your models here.
from django.utils.translation import gettext_lazy as _
from master.models import *
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from master.models import (
    Country,
    course_levels,
    current_education,
    course_requirements,
    enquiry_status,
    application_status,
    Location,
    Campus,
    Payment_Option,
    Agent_Appointment,
    EnglishTest,
    english_requirments,
    boardNotEligible,
)
def validate_max_digits(value):
    max_digits = 6  # Replace with your desired maximum number of digits
    if len(str(value)) > max_digits:
        raise ValidationError(
            _(f'The value must have a maximum of {max_digits} digits.')
        )
# Create your models here.
class UserCreatedby(models.Model):
    created_by =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_createdby", null=True)
    user_created = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    

class PhoneNumbers(models.Model):
    phone_number = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="phno")

    def __str__(self):
        return self.phone_number


class University(models.Model):
    univ_name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    univ_desc = models.CharField(max_length=1000)
    univ_logo = models.ImageField(upload_to="universitylogo", blank=True)
    univ_phone = models.CharField(max_length=50, blank=True)
    univ_email = models.EmailField(max_length=254, blank=True)
    univ_website = models.URLField(blank=True)
    assigned_users = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, default=""
    )
    active = models.BooleanField(_("Is Active"), default=True)

    class appointmemt_choices(models.TextChoices):
        YES = "YES"
        NO = "NO"
        UNIVERSITY_DISCREATION = "University Discretion"

    class yes_no_only(models.TextChoices):
        YES = "YES"
        NO = "NO"

    """GENERAL INFORMATION"""


    location = models.ManyToManyField(Location, verbose_name=_("Locations"), blank=True)
    campus = models.ManyToManyField(Campus, blank=True)
    # intake = models.ManyToManyField(intake, blank=True)
    general_documents = models.ManyToManyField(
        documents_required, related_name="university_requirements", blank=True
    )
    mandatory_docs = models.ManyToManyField(
        documents_required,
        verbose_name=_("Mandatory Document"),
        related_name="university_requirement",blank=True
    )

    finance_for_CAS = models.CharField(
        _("Finance for CAS"),
        default=True,
        blank=True,
        choices=yes_no_only.choices,
        max_length=10,
    )
    credibility_interview = models.CharField(
        _("Credibility Interview"),
        default=True,
        blank=True,
        choices=yes_no_only.choices,
        max_length=10,
    )

    offer_timeline = models.CharField(_("Offer time line"), max_length=100, null=True, blank=True)
    payment_option = models.ManyToManyField(
        Payment_Option, verbose_name=_("Payment Option"), blank=True
    )
    deposit_for_CAS = models.CharField(_("Deposit for CAS"), max_length=50, null=True, blank=True)
    scholarship = models.CharField(_("Scholarship"), max_length=100, null=True, blank=True)
    appointment_of_agent = models.CharField(
        _("Appointment of agent"), max_length=50, choices=appointmemt_choices.choices,null=True, blank=True
    )
    change_of_agent = models.CharField(
        _("Change of agent"), max_length=50, choices=appointmemt_choices.choices, null=True, blank=True
    )
    amount = models.CharField(max_length=50, blank=True, null=True)
    app_fees = models.CharField(
        _("Application Fees"), max_length=50, null=True, blank=True
    )

    dependent_acceptance = models.CharField(_("Dependent Acceptance"), max_length=100, null=True, blank=True)

    accept_case_from_high_risk = models.CharField(
        _("Accept Case from High Risk"), max_length=50,null=True, blank=True
    )
    general_visa_refusal = models.CharField(
        _("General Visa Refusal type"), max_length=100,null=True, blank=True
    )
    student_visa_refusal = models.CharField(
        _("Student Visa Refusal type"), max_length=100,null=True, blank=True
    )
    english_test = models.ManyToManyField(
        EnglishTest, verbose_name=_("English Test Accepted"), blank=True
    )
    web_link = models.URLField(default=None, null=True, blank=True)

    """ACADEMIC REQURIEMENTS"""

    english_waiver = models.PositiveIntegerField(_("English Waiver-(Percent)"),null=True, blank=True)
    english_requirement = models.ManyToManyField(
        english_requirments,blank=True
    )
    academic_requirement = models.PositiveIntegerField(
        _(" Academic Requirement General(Percent)"),
        null=True, blank=True
    )

    ielts_score = models.DecimalField(
        _("IELTS"), validators=[validate_negatives], decimal_places=1, max_digits=3, null=True, blank=True
    )
    tofel = models.DecimalField(
        _("TOFEL"), validators=[validate_negatives], decimal_places=1, max_digits=3,null=True, blank=True
    )
    pte = models.DecimalField(
        _("PTE"), validators=[validate_negatives], decimal_places=1, max_digits=3, null=True, blank=True
    )

    others = models.CharField(_("Others"), max_length=50, null=True, blank=True)
    board_not_eligible = models.ManyToManyField(
        boardNotEligible,
        verbose_name=_("Region or Boards not Eligible for English Waiver"),blank=True
    )
    gap = models.PositiveIntegerField(
        _("Education GAP (In years)"),
        default=0,
    )

    placement_option = models.CharField(
        _("Placement Option "),
        max_length=50,
        choices=yes_no_only.choices,
        default=yes_no_only.NO,
    )
    dependency_acceptance = models.CharField(
        _("Dependent Acceptance"),
        max_length=50,
        choices=yes_no_only.choices,
        default=yes_no_only.NO,
    )

    def __str__(self):
        return self.univ_name

    class Meta:
        verbose_name_plural = "Universities"


class Course(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name = 'course')
    course_name = models.CharField(max_length=100)
    course_levels = models.ForeignKey(course_levels, on_delete=models.CASCADE)
    # intake = models.ForeignKey(intake, on_delete=models.CASCADE)
    intake = models.ManyToManyField(intake)
    documents_required = models.ForeignKey(documents_required, on_delete=models.CASCADE)
    course_requirements = models.ForeignKey(
        course_requirements, on_delete=models.CASCADE
    )
    Active = models.BooleanField()

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return reverse("enquiry-detail", kwargs={"pk": self.pk})


class enquiry(models.Model):
    student_name = models.CharField(max_length=100)
    student_phone = models.CharField(max_length=20)
    student_email = models.EmailField()
    student_address = models.TextField()
    current_education = models.ForeignKey(
        current_education, on_delete=models.CASCADE, null=True, blank=True
    )
    country_interested = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True, blank=True
    )
    university_interested = models.ForeignKey(
        University,
        default = 1,
        on_delete=models.CASCADE,
        limit_choices_to={
            "active": True,
            
        },
    )
    level_applying_for = models.ForeignKey(
        course_levels, on_delete=models.CASCADE, null=True, blank=True
    )
    course_interested = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        limit_choices_to={"Active": True, "university__active": True},
        related_name="courses",
        default=32,

    )
    intake_interested = models.ForeignKey(
        intake, on_delete=models.CASCADE, null=True, blank=True
    )

    assigned_users = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        limit_choices_to={"is_active": True},
    )

    enquiry_status = models.ForeignKey(
        enquiry_status, on_delete=models.CASCADE, null=True, blank=True
    )
    added_by = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name="added_by"
    )
    notes = models.TextField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    comments = GenericRelation(Comment)

    class MarriedChoices(models.TextChoices):
        YES = True, _("Yes")
        NO = False, _("No")

    passport_number = models.CharField(
        _("Passport Number"), max_length=50, default="0000", null=True, blank=True
    )
    dob = models.DateField(
        _("Date of Birth"), auto_now=False, auto_now_add=False, null=True, blank=True
    )
    married = models.CharField(
        _("Married"),
        choices=MarriedChoices.choices,
        default=MarriedChoices.NO,
        max_length=50,
    )
    nationality = models.CharField(
        _("Nationality"), max_length=50, default="Indian", null=True, blank=True
    )
    
    country = models.CharField(
        _("Country"), max_length=50, null=True, blank=True
    )
    state = models.CharField(
        _("State"), max_length=50, null=True, blank=True
    )
    city = models.CharField(
        _("City"), max_length=50, null=True, blank=True
    )
    
    zipcode = models.PositiveIntegerField(validators=[validate_max_digits], default=123456)
    
    visa_refusal = models.BooleanField(_("Do you have any previous VISA refusal?"), default=False)
    
    visa_file = models.FileField(_("upload a file for visa refusal"), upload_to="media", null=True, blank=True)

    def __str__(self):
        return self.student_name

    class Meta:
        verbose_name_plural = "Enquiries"

    def get_absolute_url(self):
        return reverse("enquiry-detail", kwargs={"pk": self.pk})

    def LastComment(self):
        qs = Comment.objects.filter(content_type=17, object_id=self.id)
        if qs.exists():
            return qs[0]
        else:
            return "-"


# @receiver(post_save, sender=enquiry)
# def send_appointment_confirmation_email(sender, instance, created, **kwargs):
#     if created:
#         # change fail_silently = True if want to see errors while sending email.

#         send_mail(
#             'Confirmation Email',
#             "Here is the message",
#             settings.EMAIL_HOST_USER,
#             [instance.student_email, instance.assigned_users.email],
#             fail_silently= False,
#         )
#         print('email sent successfully')
#     else:
#         return


# @receiver(post_save, sender=enquiry)
# def send_notification(sender, instance, created, **kwargs):
#     notify.send(sender,
#     recipient= instance.assigned_users,
#     verb= instance.student_name,
#     description = f"A new enquiry with name {instance.student_name} has been assigned to you.",
#     # timestamp = timezone.now()
#     )
#     # notify.send(sender,recipient=instance, verb='was saved')

# post_save.connect(send_notification, sender=enquiry)
