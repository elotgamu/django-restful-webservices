# Generated by Django 3.0.4 on 2020-05-18 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dronecategory',
            options={'ordering': ('name',), 'verbose_name': 'DroneCategory', 'verbose_name_plural': 'DroneCategories'},
        ),
    ]