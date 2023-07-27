from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models
from datetime import datetime


# Create your models here.
# tutorial/models.py
class Movie(models.Model):
    # fields = ("Title", "Poster", "Genre(s)", "Rating", "Year", "Release", "Metacritic", "Rating", "Runtime")

    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)
    year = models.IntegerField()
    rated = models.CharField(max_length=10)
    released = models.CharField(max_length=50)
    runtime = models.CharField(max_length=50)
    genre = ArrayField(models.CharField(max_length=100))
    director = models.CharField(max_length=200)
    writer = models.TextField(max_length=500)
    actors = models.TextField()
    plot = models.TextField()
    language = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    awards = models.TextField()
    poster = models.URLField()
    meta_score = models.CharField(max_length=10)
    imdb_rating = models.CharField(max_length=10)
    imdb_votes = models.CharField(max_length=50)
    imdb_id = models.CharField(max_length=20)
    type = models.CharField(max_length=50)
    dvd = models.CharField(max_length=50)
    box_office = models.CharField(max_length=50)
    production = models.CharField(max_length=200)
    website = models.URLField()

    def __str__(self):
        return self.title