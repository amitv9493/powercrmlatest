from django.db import models

# Create your models here.

class Send_email(models.Model):
    from_name=models.CharField(max_length=128,verbose_name='From')
    to_name = models.CharField(max_length=128,verbose_name='To')
    cc = models.CharField(max_length=128)
    bcc = models.CharField(max_length=128)
    subject = models.CharField(max_length=128)
    email_template= models.CharField(max_length=128)
    class save_email(models.TextChoices):
       site_documents='site_documents',('site_documents')
       company_documents='company_documents',('company_documents')
    save_email_to_document_area=models.CharField(max_length=128,choices=save_email.choices,default="")

    def __str__(self):
       return self.subject
    
    class Meta:
        verbose_name_plural = "Send Emails"
        verbose_name='Send Email'
