# Generated by Django 4.1.5 on 2023-02-01 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("emails", "0002_alter_send_email_from_name_alter_send_email_to_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="send_email",
            options={
                "verbose_name": "Send Email",
                "verbose_name_plural": "Send Emails",
            },
        ),
    ]
