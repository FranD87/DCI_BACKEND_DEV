from django.db import models

class Test(models.Model):
    url = models.URLField()
    email = models.EmailField()
    slug = models.SlugField()
    json = models.JSONField(null=True)




