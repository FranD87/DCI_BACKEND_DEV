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


class Diary(models.Model):
    title = models.CharField(max_length=100)
    section = models.CharField(
        max_length=30, choices=Constants.SECTION_CHOICES, default=Constants.SECTION_CHOICES[0][0]
    )
    note = models.TextField(blank=True, default="")
    email = models.EmailField()
    author_name = models.CharField(max_length=50, blank=True, default="")
    motivation_rating = models.IntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Diary from {self.title} on {self.section}!"


'''
Model: Feedback
- Fields:
  - `name`: CharField with a maximum length of 100 characters.
  - `section`: CharField with a maximum length of 30 characters, using choices defined in `Constants.SECTION_CHOICES`. 
     The default value is the first choice in the `SECTION_CHOICES`.
  - `description`: TextField that is optional (blank) and has a default value of an empty string.
  - `email`: EmailField for storing email addresses.
  - `location`: CharField with a maximum length of 50 characters. It is optional (blank) and has a default value of 
     an empty string.
  - `rating`: IntegerField with a default value of 0. It is optional (blank).
  - `age`: IntegerField with a default value of 0. It is optional (blank).
  - `gender`: CharField with a maximum length of 10 characters, using choices defined in `Constants.GENDER_CHOICES`. 
     The default value is the first choice in the `GENDER_CHOICES`.
  - `created_at`: DateTimeField automatically set to the current date and time when the object is created.
  - `updated_at`: DateTimeField automatically updated to the current date and time whenever the object is saved.
- `__str__` method returns a string representation of the Feedback object, displaying the name and section.

Model: Diary
- Fields:
  - `title`: CharField with a maximum length of 100 characters.
  - `section`: CharField with a maximum length of 30 characters, using choices defined in `Constants.SECTION_CHOICES`. 
     The default value is the first choice in the `SECTION_CHOICES`.
  - `note`: TextField that is optional (blank) and has a default value of an empty string.
  - `email`: EmailField for storing email addresses.
  - `author_name`: CharField with a maximum length of 50 characters. It is optional (blank) and has a default value 
     of an empty string.
  - `motivation_rating`: IntegerField with a default value of 0. It is optional (blank).
  - `created_at`: DateTimeField automatically set to the current date and time when the object is created.
  - `updated_at`: DateTimeField automatically updated to the current date and time whenever the object is saved.
- `__str__` method returns a string representation of the Diary object, displaying the title and section.

These models define the structure and fields for storing feedback and diary entries in a Django database.
'''