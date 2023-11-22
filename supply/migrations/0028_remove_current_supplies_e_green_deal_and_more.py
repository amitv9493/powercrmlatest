# Generated by Django 4.2.4 on 2023-11-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0027_alter_meter_detail_e_voltage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='current_supplies',
            name='e_green_deal',
        ),
        migrations.RemoveField(
            model_name='current_supplies',
            name='e_igt_meter',
        ),
        migrations.RemoveField(
            model_name='current_supplies',
            name='g_green_deal',
        ),
        migrations.RemoveField(
            model_name='current_supplies',
            name='g_igt_meter',
        ),
        migrations.RemoveField(
            model_name='new_supplies',
            name='e_green_deal',
        ),
        migrations.RemoveField(
            model_name='new_supplies',
            name='e_igt_meter',
        ),
        migrations.RemoveField(
            model_name='new_supplies',
            name='g_green_deal',
        ),
        migrations.RemoveField(
            model_name='new_supplies',
            name='g_igt_meter',
        ),
        migrations.AlterField(
            model_name='new_supplies',
            name='e_agent',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Agent'),
        ),
        migrations.AlterField(
            model_name='new_supplies',
            name='e_contract_end_date',
            field=models.DateField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='new_supplies',
            name='e_contract_length_months',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Contract End Date'),
        ),
        migrations.AlterField(
            model_name='new_supplies',
            name='e_contract_type',
            field=models.CharField(blank=True, choices=[('ElecAMR', 'ElecAMR'), ('ElecDomestic', 'ElecDomestic'), ('ElecHH', 'ElecHH'), ('ElecHHp272', 'ElecHHp272'), ('ElecNHH', 'ElecNHH'), ('GasAMR', 'GasAMR'), ('GasCommercial', 'GasCommercial'), (' GasDomestic', 'GasDomestic')], max_length=128, null=True, verbose_name='Contract'),
        ),
        migrations.AlterField(
            model_name='new_supplies',
            name='e_customer',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='new_supplies',
            name='e_supplier_information1',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supplier Information 1'),
        ),
        migrations.AlterField(
            model_name='new_supplies',
            name='e_supplier_information2',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supplier Information 2'),
        ),
        migrations.AlterField(
            model_name='new_supplies',
            name='e_supplier_information3',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supplier Information 3'),
        ),
        migrations.AlterField(
            model_name='new_supplies',
            name='e_supplier_reference',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supplier Reference'),
        ),
        migrations.AlterField(
            model_name='new_supplies',
            name='g_supplier_reference',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supplier Reference'),
        ),
    ]