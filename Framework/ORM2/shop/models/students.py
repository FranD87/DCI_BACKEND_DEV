from django.db import models

class Students(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)
    friends = models.ManyToManyField('self', symmetrical=False)


