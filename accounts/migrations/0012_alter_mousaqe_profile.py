# Generated by Django 3.2.18 on 2023-03-25 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_mousaqe_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mousaqe',
            name='profile',
            field=models.ImageField(blank=True, default=None, upload_to='pic'),
        ),
    ]