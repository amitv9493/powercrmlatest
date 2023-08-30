# Generated by Django 4.1.7 on 2023-04-24 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('progress', '0003_alter_current_gas_progress_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_electricity_progress',
            name='completed_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
