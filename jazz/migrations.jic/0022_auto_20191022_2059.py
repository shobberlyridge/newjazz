# Generated by Django 2.2.2 on 2019-10-22 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0021_auto_20190625_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='instrument',
        ),
        migrations.AddField(
            model_name='player',
            name='instrument',
            field=models.ForeignKey(help_text='Select instrument for this player', null=True, on_delete=django.db.models.deletion.SET_NULL, to='jazz.Instrument'),
        ),
    ]
