from django.db import models


class City(models.Model):
    COUNTRIES = [
        ('UK', 'United Kingdom'),
        ('UA', 'Ukraine'),
        ('DE', 'Deutschland')
    ]
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=2, choices=COUNTRIES)



    
