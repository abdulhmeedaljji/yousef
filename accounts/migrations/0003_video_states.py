# Generated by Django 4.1.4 on 2023-03-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_video_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='states',
            field=models.BooleanField(default=False),
        ),
    ]
