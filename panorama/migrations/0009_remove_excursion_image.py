# Generated by Django 4.1.2 on 2023-02-25 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panorama', '0008_excursion_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='excursion',
            name='image',
        ),
    ]
