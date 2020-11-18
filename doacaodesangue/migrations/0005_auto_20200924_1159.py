# Generated by Django 3.1.1 on 2020-09-24 14:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doacaodesangue', '0004_auto_20200924_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doador',
            name='CPF',
        ),
        migrations.AddField(
            model_name='doador',
            name='RG',
            field=models.CharField(default=12, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doador',
            name='idade',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]