# Generated by Django 4.2.2 on 2023-08-14 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_company_addressline1_company_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='contact_title',
        ),
        migrations.RemoveField(
            model_name='company',
            name='primary_contact_email',
        ),
        migrations.RemoveField(
            model_name='company',
            name='primary_contact_first_name',
        ),
        migrations.RemoveField(
            model_name='company',
            name='primary_contact_last_name',
        ),
        migrations.RemoveField(
            model_name='company',
            name='primary_contact_position',
        ),
        migrations.RemoveField(
            model_name='company',
            name='telephone_number',
        ),
    ]