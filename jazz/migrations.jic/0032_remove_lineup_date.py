# Generated by Django 2.2.2 on 2020-06-08 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0031_auto_20200608_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineup',
            name='date',
        ),
    ]