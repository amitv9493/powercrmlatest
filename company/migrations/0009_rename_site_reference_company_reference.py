# Generated by Django 4.2.2 on 2023-08-24 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_company_parent_company_company_site_reference'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='site_reference',
            new_name='reference',
        ),
    ]
