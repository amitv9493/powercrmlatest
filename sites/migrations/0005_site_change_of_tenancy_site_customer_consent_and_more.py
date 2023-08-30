# Generated by Django 4.1.7 on 2023-04-10 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_company_address_alter_company_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0004_rename_addressline1_site_addressline1_billing_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='change_of_tenancy',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='CoT'),
        ),
        migrations.AddField(
            model_name='site',
            name='customer_consent',
            field=models.BooleanField(default=False, verbose_name='Please confirm customer consent has been received to be contacted regarding the current quote'),
        ),
        migrations.AddField(
            model_name='site',
            name='tenant',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='site',
            name='vacant',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='site',
            name='addressline1_billing',
            field=models.CharField(max_length=128, verbose_name='addressline 1'),
        ),
        migrations.AlterField(
            model_name='site',
            name='addressline1_site',
            field=models.CharField(max_length=128, verbose_name='address line 1'),
        ),
        migrations.AlterField(
            model_name='site',
            name='addressline2_billing',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='addressline 2'),
        ),
        migrations.AlterField(
            model_name='site',
            name='addressline2_site',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='address line 2'),
        ),
        migrations.AlterField(
            model_name='site',
            name='addressline3_billing',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='addressline 3'),
        ),
        migrations.AlterField(
            model_name='site',
            name='addressline3_site',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='address line 3'),
        ),
        migrations.AlterField(
            model_name='site',
            name='addressline4_billing',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='addressline 4'),
        ),
        migrations.AlterField(
            model_name='site',
            name='addressline4_site',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='address line 4'),
        ),
        migrations.AlterField(
            model_name='site',
            name='bill_to_sent',
            field=models.BooleanField(default=False, verbose_name='Bill to Site'),
        ),
        migrations.AlterField(
            model_name='site',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company', verbose_name='Company Name'),
        ),
        migrations.AlterField(
            model_name='site',
            name='country_billing',
            field=models.CharField(max_length=128, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='site',
            name='country_site',
            field=models.CharField(max_length=128, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='site',
            name='lead_source',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='notes',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='parent_company',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Parent Company (Optional)'),
        ),
        migrations.AlterField(
            model_name='site',
            name='postcode_billing',
            field=models.CharField(max_length=128, verbose_name='Postcode'),
        ),
        migrations.AlterField(
            model_name='site',
            name='postcode_site',
            field=models.CharField(max_length=128, verbose_name='Postcode'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_reference',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='site',
            name='support_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='site',
            name='welcome_letter_send',
            field=models.BooleanField(default=False, verbose_name='Welcome Letter Sent'),
        ),
    ]
