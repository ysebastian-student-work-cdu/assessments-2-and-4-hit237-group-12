# Generated by Django 4.2 on 2023-05-30 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_rename_name_waste_types_inedible_waste_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food_items',
            old_name='description',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='food_items',
            old_name='ingredients',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='food_items',
            old_name='instructions',
            new_name='reason',
        ),
    ]
