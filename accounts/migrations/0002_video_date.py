# Generated by Django 4.1.4 on 2023-03-22 20:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]