# Generated by Django 2.2.2 on 2019-06-16 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0008_auto_20190616_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineup',
            name='band_name',
            field=models.CharField(max_length=100),
        ),
    ]
