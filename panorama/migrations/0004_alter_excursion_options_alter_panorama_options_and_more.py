# Generated by Django 4.1.2 on 2023-02-24 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panorama', '0003_auto_20230224_1726'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='excursion',
            options={'verbose_name': 'Excursion', 'verbose_name_plural': 'Excursions'},
        ),
        migrations.AlterModelOptions(
            name='panorama',
            options={'verbose_name': 'Panorama', 'verbose_name_plural': 'Panoramas'},
        ),
        migrations.AlterField(
            model_name='panorama',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
