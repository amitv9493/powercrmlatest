# Generated by Django 4.2.4 on 2023-11-20 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0025_rename_contract_length_months_new_supplies_g_contract_length_months_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new_supplies',
            old_name='notes',
            new_name='e_notes',
        ),
        migrations.AddField(
            model_name='new_supplies',
            name='g_notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
