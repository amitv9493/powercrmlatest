# Generated by Django 4.1.7 on 2023-04-21 10:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0020_alter_company_reminder_alert_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_reminder',
            name='alert',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 21, 10, 19, 54, 917250), verbose_name='Alert Date and Time '),
        ),
        migrations.AlterField(
            model_name='general_reminder',
            name='alert',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 21, 10, 19, 54, 917250), verbose_name='Alert Date and Time '),
        ),
        migrations.AlterField(
            model_name='site_reminder',
            name='alert',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 21, 10, 19, 54, 917250), verbose_name='Alert Date and Time '),
        ),
    ]
