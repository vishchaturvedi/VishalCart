# Generated by Django 3.0.4 on 2020-04-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200406_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='phone',
            field=models.IntegerField(max_length=9999999999),
        ),
    ]
