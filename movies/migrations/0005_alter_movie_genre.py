# Generated by Django 4.2.3 on 2023-07-27 09:02

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('movies', '0004_alter_movie_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None),
        ),
    ]
