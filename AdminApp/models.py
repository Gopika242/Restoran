from django.db import models


# Create your models here.

class CuisineDb(models.Model):
    CuisineName = models.CharField(max_length=100, null=True, blank=True)
    Description = models.TextField(max_length=100, null=True, blank=True)
    CuisineImage = models.ImageField(upload_to='Cuisine', null=True, blank=True)


class DishDb(models.Model):
    Cuisine = models.CharField(max_length=100, null=True, blank=True)
    DishName = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    About = models.TextField(max_length=100, null=True, blank=True)
    DishImage = models.ImageField(upload_to='Dish', null=True, blank=True)
