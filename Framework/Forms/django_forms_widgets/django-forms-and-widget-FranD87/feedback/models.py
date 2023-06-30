from django.db import models
from .enums import Constants


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(
        max_length=30, choices=Constants.SECTION_CHOICES, default=Constants.SECTION_CHOICES[0][0]
    )
    description = models.TextField(blank=True, default="")
    email = models.EmailField()
    location = models.CharField(max_length=50, blank=True, default="")
    rating = models.IntegerField(default=0, blank=True)
    age = models.IntegerField(default=0, blank=True)
    gender = models.CharField(
        max_length=10, choices=Constants.GENDER_CHOICES, default=Constants.GENDER_CHOICES[0][0]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Feedback from {self.name} on {self.section}!"
