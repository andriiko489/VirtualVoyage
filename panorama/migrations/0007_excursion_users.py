# Generated by Django 4.1.2 on 2023-02-25 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_bio'),
        ('panorama', '0006_remove_excursion_users_alter_panorama_excursion'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursion',
            name='users',
            field=models.ManyToManyField(blank=True, to='users.profile'),
        ),
    ]
