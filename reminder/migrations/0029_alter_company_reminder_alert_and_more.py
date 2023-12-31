# Generated by Django 4.2.2 on 2023-06-23 07:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0028_alter_company_reminder_alert_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_reminder',
            name='alert',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 12, 44, 33, 67179), verbose_name='Alert Date and Time '),
        ),
        migrations.AlterField(
            model_name='general_reminder',
            name='alert',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 12, 44, 33, 66179), verbose_name='Alert Date and Time '),
        ),
        migrations.AlterField(
            model_name='site_reminder',
            name='alert',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 12, 44, 33, 67179), verbose_name='Alert Date and Time '),
        ),
    ]
