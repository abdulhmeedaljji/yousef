# Generated by Django 3.2.18 on 2023-03-25 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_mousaqe_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='mousaqe',
            name='profile',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='pic'),
        ),
    ]
