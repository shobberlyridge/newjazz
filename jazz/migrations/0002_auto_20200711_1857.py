# Generated by Django 2.2.2 on 2020-07-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='slug',
            field=models.SlugField(max_length=125, unique=True),
        ),
    ]
