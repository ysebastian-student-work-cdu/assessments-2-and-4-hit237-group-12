from django.db import models

# Create your models here.

class Food_waste_Audit(models.Model):
    date = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    auditor = models.TextField()
    waste_amount = models.TextField()

    def __str__(self):
        return self.date


class Food_Items(models.Model):
    name = models.CharField(max_length=200)
    category = models.TextField()
    quantity = models.TextField()
    reason = models.TextField()

    def __str__(self):
        return self.name

class Waste_Types(models.Model):
    inedible_waste = models.CharField(max_length=200)
    spoilage_waste = models.TextField()
    preparation_waste = models.TextField()
    plate_buffet = models.TextField()
    items = models.ManyToManyField(Food_waste_Audit, related_name='unused_field')

    def __str__(self):
        return self.inedible_waste