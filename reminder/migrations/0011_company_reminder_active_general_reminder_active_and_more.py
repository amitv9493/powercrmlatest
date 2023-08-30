# Generated by Django 4.1.7 on 2023-04-17 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0010_alter_company_reminder_alert_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_reminder',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='general_reminder',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='site_reminder',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='company_reminder',
            name='alert',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 17, 10, 31, 1, 892806), verbose_name='Alert Date and Time '),
        ),
        migrations.AlterField(
            model_name='general_reminder',
            name='alert',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 17, 10, 31, 1, 889935), verbose_name='Alert Date and Time '),
        ),
        migrations.AlterField(
            model_name='site_reminder',
            name='alert',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 17, 10, 31, 1, 892806), verbose_name='Alert Date and Time '),
        ),
    ]
