
# Generated by Django 4.2.2 on 2023-08-28 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_alter_company_account_name_alter_company_account_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='parent_company',
            field=models.CharField(blank=True, help_text='Optional', max_length=128, null=True),
        ),
    ]