# Generated by Django 3.0.5 on 2020-04-06 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('description', models.CharField(max_length=55)),
                ('price', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.URLField()),
                ('phone', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
