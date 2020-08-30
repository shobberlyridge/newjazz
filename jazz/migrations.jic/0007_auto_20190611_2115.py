# Generated by Django 2.2.2 on 2019-06-11 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0006_lineup'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='lineup',
            constraint=models.UniqueConstraint(fields=('band_name', 'date'), name='unique_lineup'),
        ),
    ]