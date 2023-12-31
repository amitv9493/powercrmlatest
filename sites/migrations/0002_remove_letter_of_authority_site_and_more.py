# Generated by Django 4.1.7 on 2023-04-07 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0002_alter_company_address_alter_company_name'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter_of_authority',
            name='site',
        ),
        migrations.RemoveField(
            model_name='our_detail',
            name='site',
        ),
        migrations.RemoveField(
            model_name='our_detail',
            name='support_contact',
        ),
        migrations.RemoveField(
            model_name='site_address',
            name='site',
        ),
        migrations.RemoveField(
            model_name='site_detail',
            name='company',
        ),
        migrations.RemoveField(
            model_name='site_detail',
            name='site',
        ),
        migrations.AddField(
            model_name='site',
            name='addressline1',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='addressline2',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='addressline3',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='addressline4',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='agent_email',
            field=models.EmailField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='bill_to_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='site',
            name='country',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='current_gas_and_electricity_supplier_details',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='lead_source',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='lead_typee',
            field=models.CharField(choices=[('GAS', 'GAS'), ('ELECTRICITY', 'ELECTRICITY')], default='', max_length=128),
        ),
        migrations.AddField(
            model_name='site',
            name='loa_header_to_use',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='loa_template',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='notes',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='owner_name',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='parent_company',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='postcode',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='site_name',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='site_reference',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='support_contact',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='type_of_owner',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='welcome_letter_send',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='site',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
        migrations.DeleteModel(
            name='Billing_address',
        ),
        migrations.DeleteModel(
            name='Letter_of_authority',
        ),
        migrations.DeleteModel(
            name='Our_detail',
        ),
        migrations.DeleteModel(
            name='Site_address',
        ),
        migrations.DeleteModel(
            name='Site_detail',
        ),
    ]
