from django.db import models

class Logo(models.Model):
    logo = models.FilePathField(path='logo')


