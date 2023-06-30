from django.db import models


class Photo(models.Model):
    state = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photo')




