from django.db import models
from shop.models.user import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    info = models.CharField(max_length=255)
