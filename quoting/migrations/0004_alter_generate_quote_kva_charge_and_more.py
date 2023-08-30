# Generated by Django 4.1.4 on 2022-12-15 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoting', '0003_alter_generate_quote_kva_charge_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generate_quote',
            name='kva_charge',
            field=models.FloatField(max_length=128, verbose_name='Standing Charge(pence)'),
        ),
        migrations.AlterField(
            model_name='generate_quote',
            name='standing_charge',
            field=models.FloatField(max_length=128, verbose_name='Standing Charge(pence)'),
        ),
    ]
