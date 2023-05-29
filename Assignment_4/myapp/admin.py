from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Food_waste_Audit)
admin.site.register(Food_Items)
admin.site.register(Waste_Types)