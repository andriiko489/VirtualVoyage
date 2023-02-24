from django.db import models
class Excursion(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

class Panorama(models.Model):
    description = models.CharField(max_length=200)
    image = models.ImageField()
    excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE)
