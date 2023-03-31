# Generated by Django 4.1.4 on 2023-03-23 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_file_after_tranlated_mousaqe'),
    ]

    operations = [
        migrations.CreateModel(
            name='citys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='mousaqe',
            name='address',
        ),
        migrations.CreateModel(
            name='earas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eara', models.CharField(max_length=150)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.citys')),
            ],
        ),
        migrations.AddField(
            model_name='mousaqe',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.citys'),
        ),
        migrations.AddField(
            model_name='mousaqe',
            name='eara',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.earas'),
        ),
    ]
