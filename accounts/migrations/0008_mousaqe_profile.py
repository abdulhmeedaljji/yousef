# Generated by Django 3.2.18 on 2023-03-25 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_file_after_tranlated_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='mousaqe',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='pic'),
        ),
    ]
