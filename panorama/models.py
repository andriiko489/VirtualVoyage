from django.db import models
class Excursion(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    is_private = models.BooleanField(default=0)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Excursions'
        verbose_name = 'Excursion'

class Panorama(models.Model):
    description = models.CharField(max_length=200)
    image = models.ImageField()
    excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE)
    def __str__(self):
        return self.description
    class Meta:
        verbose_name_plural = 'Panoramas'
        verbose_name = 'Panorama'
