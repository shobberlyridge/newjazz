# Generated by Django 2.2.2 on 2019-06-16 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0009_auto_20190616_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineup',
            name='band_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jazz.Band'),
        ),
    ]
