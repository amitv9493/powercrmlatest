# Generated by Django 4.1.7 on 2023-04-12 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0011_site_loa_template'),
        ('supply', '0012_alter_meter_detail_e_green_deal_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supply_detail',
            name='current_supplies',
        ),
        migrations.RemoveField(
            model_name='supply_detail',
            name='meter_detail',
        ),
        migrations.RemoveField(
            model_name='supply_detail',
            name='new_supplies',
        ),
        migrations.RemoveField(
            model_name='current_supplies',
            name='electricity_current_supplies',
        ),
        migrations.RemoveField(
            model_name='current_supplies',
            name='gas_current_supplies',
        ),
        migrations.RemoveField(
            model_name='new_supplies',
            name='electricity_new_supplies',
        ),
        migrations.RemoveField(
            model_name='new_supplies',
            name='gas_new_supplies',
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='e_agent',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Agent'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='e_contract_back_date',
            field=models.DateField(blank=True, null=True, verbose_name='Contract Back Date'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='e_contract_end_date',
            field=models.DateField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='e_contract_length_months',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Contract End Date'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='e_contract_start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Contract Start Date'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='e_contract_type',
            field=models.CharField(blank=True, choices=[('ElecAMR', 'ElecAMR'), ('ElecDomestic', 'ElecDomestic'), ('ElecHH', 'ElecHH'), ('ElecHHp272', 'ElecHHp272'), ('ElecNHH', 'ElecNHH'), ('GasAMR', 'GasAMR'), ('GasCommercial', 'GasCommercial'), (' GasDomestic', 'GasDomestic')], max_length=128, null=True, verbose_name='Contract'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='e_customer',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Customer'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='e_green_deal',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Green Deal'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='e_igt_meter',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='IGT Meter'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='e_product',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='e_supplier',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supplier'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='e_supplier_information1',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supplier Information 1'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='e_supplier_information2',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supplier Information 2'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='e_supplier_information3',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supplier Information 3'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='e_supplier_reference',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supplier Reference'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='e_won_date',
            field=models.DateField(blank=True, null=True, verbose_name='Won Date'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='g_agent',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Agent'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='g_contract_back_date',
            field=models.DateField(blank=True, null=True, verbose_name='Contract Back Date'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='g_contract_end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Contract End Date'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='g_contract_length_months',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Contract Length (Months)'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='g_contract_start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Contract Start Date'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='g_contract_type',
            field=models.CharField(blank=True, choices=[('ElecAMR', 'ElecAMR'), ('ElecDomestic', 'ElecDomestic'), ('ElecHH', 'ElecHH'), ('ElecHHp272', 'ElecHHp272'), ('ElecNHH', 'ElecNHH'), ('GasAMR', 'GasAMR'), ('GasCommercial', 'GasCommercial'), (' GasDomestic', 'GasDomestic')], max_length=128, null=True, verbose_name='Contract Type'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='g_customer',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Customer'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='g_green_deal',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Green Deal'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='g_igt_meter',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='IGT Meter'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='g_product',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='g_supplier',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supplier'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='g_supplier_information1',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supplier Information 1'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='g_supplier_information2',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supplier Information 2'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='g_supplier_information3',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supplier Information 3'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='g_supplier_reference',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supplier Reference'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='g_won_date',
            field=models.DateField(blank=True, null=True, verbose_name='Won Date'),
        ),
        migrations.AddField(
            model_name='current_supplies',
            name='site',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='contract_length_months',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Contract Length (Months)'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='e_agent',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Agent'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='e_contract_back_date',
            field=models.DateField(blank=True, null=True, verbose_name='Contract Back Date'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='e_contract_end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Contract End Date'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='e_contract_length_months',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Contract Length months'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='e_contract_start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Contract Start Date'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='e_contract_type',
            field=models.CharField(blank=True, choices=[('ElecAMR', 'ElecAMR'), ('ElecDomestic', 'ElecDomestic'), ('ElecHH', 'ElecHH'), ('ElecHHp272', 'ElecHHp272'), ('ElecNHH', 'ElecNHH'), ('GasAMR', 'GasAMR'), ('GasCommercial', 'GasCommercial'), (' GasDomestic', 'GasDomestic')], max_length=128, null=True, verbose_name='Contract Type'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='e_customer',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Customer'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='e_green_deal',
            field=models.BooleanField(default=None, verbose_name='green Deal'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='e_igt_meter',
            field=models.BooleanField(default=None, verbose_name='IGT Meter'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='e_product',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='e_supplier',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='e_supplier_information1',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name=' Supplier Information 1'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='e_supplier_information2',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name=' Supplier Information 2'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='e_supplier_information3',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name=' Supplier Information 3'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='e_supplier_reference',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supplier reference'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='e_won_date',
            field=models.DateField(blank=True, null=True, verbose_name='Won Date'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='g_agent',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Agent'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='g_contract_back_date',
            field=models.DateField(blank=True, null=True, verbose_name='Contract Back Date'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='g_contract_end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Contract End Date'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='g_contract_start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Contract Start Date'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='g_contract_type',
            field=models.CharField(blank=True, choices=[('ElecAMR', 'ElecAMR'), ('ElecDomestic', 'ElecDomestic'), ('ElecHH', 'ElecHH'), ('ElecHHp272', 'ElecHHp272'), ('ElecNHH', 'ElecNHH'), ('GasAMR', 'GasAMR'), ('GasCommercial', 'GasCommercial'), (' GasDomestic', 'GasDomestic')], max_length=128, null=True, verbose_name='Contract Type'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='g_customer',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Customer'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='g_green_deal',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Green Deal'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='g_igt_meter',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='IGT Meter'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='g_product',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='g_supplier',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='g_supplier_information1',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supplier Information 1'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='g_supplier_information2',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supplier Information 2'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='g_supplier_information3',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supplier Information 3'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='g_supplier_reference',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supply Reference'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='g_won_date',
            field=models.DateField(blank=True, null=True, verbose_name='Won Date'),
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='site',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='e_capacity',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Capacity'),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='e_green_deal',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Green Deal'),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='e_ley_meter',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Key Meter'),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='e_measurement_class',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Measurement Class'),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='e_meter_type',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Meter Type'),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='e_mpan_bottomline',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='MPAN Bottomline'),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='e_mpan_topline',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='MPAN Topline'),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='e_related_meter',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Related Meter'),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='e_serial_number',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Serial Number'),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='e_smart_meter',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Smart Meter'),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='g_green_deal',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Green Deal'),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='g_igt_meter',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='IGT Meter'),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='g_mpr',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='MPR'),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='g_serial_number',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Serial Number'),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='g_smart_meter',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Smart Meter'),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='site',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Electricity_current_supplies',
        ),
        migrations.DeleteModel(
            name='Electricity_new_supplies',
        ),
        migrations.DeleteModel(
            name='Gas_current_supplies',
        ),
        migrations.DeleteModel(
            name='Gas_new_supplies',
        ),
        migrations.DeleteModel(
            name='Supply_detail',
        ),
    ]
