# Generated by Django 2.2.2 on 2019-06-25 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0020_auto_20190625_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='lineup',
            field=models.ManyToManyField(related_name='toLineups', to='jazz.Lineup'),
        ),
    ]
