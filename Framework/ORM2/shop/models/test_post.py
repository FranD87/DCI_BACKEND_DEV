from django.db import models
from shop.models.user import User

class TestPost(models.Model):
    title = models.CharField(max_length=255)
    info = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='email')

