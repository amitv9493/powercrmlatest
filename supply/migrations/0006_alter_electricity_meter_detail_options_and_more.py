# Generated by Django 4.1.7 on 2023-04-11 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0005_alter_electricity_meter_detail_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='electricity_meter_detail',
            options={'verbose_name': 'Electricity meter detail', 'verbose_name_plural': 'Electricity meter detail'},
        ),
        migrations.AlterModelOptions(
            name='meter_detail',
            options={'verbose_name': 'Meter Detail'},
        ),
        migrations.AlterField(
            model_name='electricity_meter_detail',
            name='meter_detail',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='e_detail', to='supply.meter_detail'),
        ),
        migrations.AlterField(
            model_name='gas_meter_detail',
            name='meter_detail',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='g_detail', to='supply.meter_detail'),
        ),
    ]
