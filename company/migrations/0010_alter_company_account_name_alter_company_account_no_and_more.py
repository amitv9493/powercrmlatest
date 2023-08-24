# Generated by Django 4.2.2 on 2023-08-24 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_rename_site_reference_company_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='account_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='account_no',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='bank_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='business_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.business_type', verbose_name='Company Type'),
        ),
        migrations.AlterField(
            model_name='company',
            name='estimated_turnover',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='home_post_code',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='number_of_employees',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='partner_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='registration_no',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='shortcode',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
