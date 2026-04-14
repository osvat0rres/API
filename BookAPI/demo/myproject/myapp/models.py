from django.db import models

# Create your models here.

class BookMenu(models.Model):
    tittle = models.CharField(max_length=200)
    author = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()