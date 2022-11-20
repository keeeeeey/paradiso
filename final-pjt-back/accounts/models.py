from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie

class User(AbstractUser):
    email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    nickname = models.CharField(max_length=100, null=False, blank=False, unique=True)
    isFirst = models.BooleanField(default=True)
    favorite_movies = models.ManyToManyField(Movie, related_name="favorite_user")
    hate_movies = models.ManyToManyField(Movie, related_name="hate_user")
    followings = models.ManyToManyField("self", symmetrical=False, related_name="followers")