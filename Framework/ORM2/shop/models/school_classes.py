from django.db import models
from shop.models.students import Students

class Class(models.Model):
    title = models.CharField(max_length=255)
    info = models.TextField()
    student = models.ManyToManyField(Students, related_name='attends')

