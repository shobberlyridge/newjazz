# Generated by Django 2.2.2 on 2020-06-08 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0027_auto_20200607_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='lineup',
        ),
    ]
