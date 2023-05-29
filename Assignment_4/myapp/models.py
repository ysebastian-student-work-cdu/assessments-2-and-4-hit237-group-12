from django.db import models

# Create your models here.

class Food_waste_Audit(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.TextField()

    def __str__(self):
        return self.name


class Food_Items(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.name

class Waste_Types(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    restaurant = models.TextField()
    items = models.ManyToManyField(Food_waste_Audit, related_name='unused_field')

    def __str__(self):
        return self.name