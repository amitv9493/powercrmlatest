# Generated by Django 4.1.7 on 2023-04-21 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0004_remove_company_document_site_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_document',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='general_document',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='site_document',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
