# Generated by Django 4.2.4 on 2023-11-21 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0026_rename_notes_new_supplies_e_notes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meter_detail',
            name='e_voltage',
            field=models.FloatField(null=True, verbose_name='Voltage'),
        ),
    ]
