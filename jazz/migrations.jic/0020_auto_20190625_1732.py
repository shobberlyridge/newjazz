# Generated by Django 2.2.2 on 2019-06-25 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0019_auto_20190625_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineup',
            name='player',
            field=models.ManyToManyField(related_name='toPlayer', to='jazz.Player'),
        ),
    ]