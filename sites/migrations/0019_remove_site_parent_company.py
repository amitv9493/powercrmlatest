# Generated by Django 4.2.2 on 2023-08-28 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0018_alter_site_current_gas_and_electricity_supplier_details_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='parent_company',
        ),
    ]
