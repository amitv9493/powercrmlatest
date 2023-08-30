# Generated by Django 4.1.7 on 2023-04-14 08:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0011_site_loa_template'),
        ('reminder', '0005_rename_company_site_reminder_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_reminder',
            name='alert_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 14, 8, 45, 2, 218709, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='site_reminder',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='Select Site'),
        ),
    ]
