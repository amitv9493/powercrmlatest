# Generated by Django 4.1.7 on 2023-04-18 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0011_site_loa_template'),
        ('supply', '0021_alter_meter_detail_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='current_supplies',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
        ),
        migrations.AlterField(
            model_name='new_supplies',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
        ),
    ]
