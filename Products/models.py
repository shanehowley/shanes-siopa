from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Product(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to="images", blank=True, null=True)
    tag = models.CharField(max_length=30, blank=True, null=True)
    rating = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

