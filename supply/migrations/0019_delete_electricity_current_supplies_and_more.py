# Generated by Django 4.1.7 on 2023-04-14 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0018_remove_old_meter_detail_electricity_meter_detail_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Electricity_current_supplies',
        ),
        migrations.DeleteModel(
            name='Electricity_meter_detail',
        ),
        migrations.DeleteModel(
            name='Electricity_new_supplies',
        ),
        migrations.DeleteModel(
            name='Gas_current_supplies',
        ),
        migrations.DeleteModel(
            name='Gas_meter_detail',
        ),
        migrations.DeleteModel(
            name='Gas_new_supplies',
        ),
    ]
