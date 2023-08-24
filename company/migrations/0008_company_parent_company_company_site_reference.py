# Generated by Django 4.2.2 on 2023-08-24 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_remove_company_credit_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='parent_company',
            field=models.ForeignKey(blank=True, help_text='Optional', null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.company'),
        ),
        migrations.AddField(
            model_name='company',
            name='site_reference',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
