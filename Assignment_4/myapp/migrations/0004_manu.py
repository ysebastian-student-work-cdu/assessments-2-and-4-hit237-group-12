# Generated by Django 4.2.1 on 2023-05-13 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_recipe_delete_menuitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('ingredients', models.TextField()),
                ('restaurant', models.TextField()),
            ],
        ),
    ]