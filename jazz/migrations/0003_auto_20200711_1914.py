# Generated by Django 2.2.2 on 2020-07-11 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0002_auto_20200711_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineup',
            name='slug',
            field=models.SlugField(blank=True, max_length=125, unique=True),
        ),
    ]