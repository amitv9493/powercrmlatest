# Generated by Django 4.1.7 on 2023-04-12 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0009_remove_gas_meter_detail_meter_detail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meter_detail',
            name='e_capacity',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='e_measurement_class',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='e_meter_type',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='e_mpan_bottomline',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='e_mpan_topline',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='e_serial_number',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='g_mpr',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='g_serial_number',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
