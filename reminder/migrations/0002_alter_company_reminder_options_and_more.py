# Generated by Django 4.1.5 on 2023-02-01 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reminder", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="company_reminder",
            options={
                "verbose_name": "Company Reminder",
                "verbose_name_plural": "Company Reminders",
            },
        ),
        migrations.AlterModelOptions(
            name="general_reminder",
            options={
                "verbose_name": "General Reminder",
                "verbose_name_plural": "General Reminders",
            },
        ),
        migrations.AlterModelOptions(
            name="site_reminder",
            options={
                "verbose_name": "Site Reminder",
                "verbose_name_plural": "Site Reminders",
            },
        ),
    ]
