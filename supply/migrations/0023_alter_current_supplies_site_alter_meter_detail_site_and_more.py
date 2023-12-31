# Generated by Django 4.2.4 on 2023-11-20 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0019_remove_site_parent_company'),
        ('supply', '0022_alter_current_supplies_site_alter_new_supplies_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='current_supplies',
            name='site',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
        ),
        migrations.AlterField(
            model_name='meter_detail',
            name='site',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
        ),
        migrations.AlterField(
            model_name='new_supplies',
            name='site',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
        ),
    ]
