# Generated by Django 3.2.18 on 2023-03-25 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_mousaqe_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mousaqe',
            name='profile',
        ),
    ]