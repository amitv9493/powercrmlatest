# Generated by Django 4.2.2 on 2023-08-22 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0009_user_credentials_access_token_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_credentials',
            name='access_token',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user_credentials',
            name='refresh_token',
            field=models.TextField(),
        ),
    ]
