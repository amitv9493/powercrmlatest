# Generated by Django 4.1.4 on 2022-12-19 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_date', models.DateField()),
                ('alert_time', models.TimeField()),
                ('priority', models.IntegerField()),
                ('reminder_type', models.CharField(choices=[('Callback', 'Callback'), ('Quotecallback', 'Quotecallback'), ('Fsocallback', 'Fsocallback'), ('Renewalcallback', 'Renewalcallback'), ('Other', 'Other')], max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='General_Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_date', models.DateField()),
                ('alert_time', models.TimeField()),
                ('priority', models.IntegerField()),
                ('reminder_type', models.CharField(choices=[('Callback', 'Callback'), ('Quotecallback', 'Quotecallback'), ('Fsocallback', 'Fsocallback'), ('Renewalcallback', 'Renewalcallback'), ('Other', 'Other')], max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Site_Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_date', models.DateField()),
                ('alert_time', models.TimeField()),
                ('priority', models.IntegerField()),
                ('reminder_type', models.CharField(choices=[('Callback', 'Callback'), ('Quotecallback', 'Quotecallback'), ('Fsocallback', 'Fsocallback'), ('Renewalcallback', 'Renewalcallback'), ('Other', 'Other')], max_length=128)),
            ],
        ),
    ]
