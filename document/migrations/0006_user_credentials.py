# Generated by Django 4.2.2 on 2023-08-22 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('document', '0005_company_document_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_credentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('selling_partner_id', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='')),
            ],
        ),
    ]
