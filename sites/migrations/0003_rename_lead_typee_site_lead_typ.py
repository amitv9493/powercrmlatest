# Generated by Django 4.1.7 on 2023-04-07 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_remove_letter_of_authority_site_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='lead_typee',
            new_name='lead_typ',
        ),
    ]
