# Generated by Django 3.0.4 on 2020-04-08 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200408_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='name',
            field=models.CharField(max_length=55),
        ),
    ]
