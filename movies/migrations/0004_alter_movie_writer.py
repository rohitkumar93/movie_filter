# Generated by Django 4.2.3 on 2023-07-27 07:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('movies', '0003_alter_movie_date_alter_movie_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='writer',
            field=models.TextField(max_length=500),
        ),
    ]
