from django.db import models

# Create your models here.

class Movie(models.Model):
    '''Item Model'''
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=10)
    year = models.IntegerField()# null=True by default
    director = models.CharField(max_length=100)
    genre = models.TextField(max_length=20)