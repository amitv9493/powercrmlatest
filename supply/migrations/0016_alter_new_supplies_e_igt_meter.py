# Generated by Django 4.1.7 on 2023-04-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0015_alter_new_supplies_e_green_deal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_supplies',
            name='e_igt_meter',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='IGT Meter'),
        ),
    ]
