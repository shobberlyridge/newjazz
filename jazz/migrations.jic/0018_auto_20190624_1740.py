# Generated by Django 2.2.2 on 2019-06-24 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0017_auto_20190624_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineup',
            name='player',
        ),
        migrations.RemoveField(
            model_name='player',
            name='lineup',
        ),
    ]