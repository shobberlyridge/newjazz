# Generated by Django 2.2.2 on 2019-06-17 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0012_auto_20190617_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineup',
            name='player',
        ),
    ]
