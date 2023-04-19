from django.db import models

# Create your models here.

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description