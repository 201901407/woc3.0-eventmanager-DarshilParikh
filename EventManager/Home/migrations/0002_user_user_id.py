# Generated by Django 3.1.4 on 2021-01-11 10:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.CharField(default=uuid.uuid4, max_length=100),
        ),
    ]
