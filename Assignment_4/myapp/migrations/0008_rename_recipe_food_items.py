# Generated by Django 4.2 on 2023-05-29 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_food_waste_food_waste_audit'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recipe',
            new_name='Food_Items',
        ),
    ]
