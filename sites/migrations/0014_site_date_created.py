# Generated by Django 4.2.2 on 2023-06-23 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0013_group_alter_site_group_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
