# Generated by Django 3.1.4 on 2021-01-19 10:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_event_registration_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='registration_deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]