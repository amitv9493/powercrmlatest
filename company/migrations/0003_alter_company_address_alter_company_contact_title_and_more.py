# Generated by Django 4.1.7 on 2023-04-10 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_company_address_alter_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='contact_title',
            field=models.CharField(choices=[('Sir', 'Sir'), ('Mr', 'Mr'), ('Ms', 'Ms'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Dr', 'Dr')], max_length=128),
        ),
        migrations.AlterField(
            model_name='company',
            name='home_post_code',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='company',
            name='partner_name',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='company',
            name='time_at_address_months',
            field=models.PositiveIntegerField(blank=True, verbose_name='Time At Address(months)'),
        ),
        migrations.AlterField(
            model_name='company',
            name='time_at_address_years',
            field=models.PositiveIntegerField(blank=True, verbose_name='Time At Address(years)'),
        ),
    ]
