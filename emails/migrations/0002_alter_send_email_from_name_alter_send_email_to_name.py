# Generated by Django 4.1.4 on 2022-12-19 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='send_email',
            name='from_name',
            field=models.CharField(max_length=128, verbose_name='From'),
        ),
        migrations.AlterField(
            model_name='send_email',
            name='to_name',
            field=models.CharField(max_length=128, verbose_name='To'),
        ),
    ]
