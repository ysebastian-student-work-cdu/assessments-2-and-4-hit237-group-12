# Generated by Django 4.2 on 2023-05-29 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_restaurant_food_waste'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Food_waste',
            new_name='Food_waste_Audit',
        ),
    ]
