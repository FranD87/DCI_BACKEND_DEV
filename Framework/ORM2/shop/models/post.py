from django.db import models
from shop.models.user import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    post = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

