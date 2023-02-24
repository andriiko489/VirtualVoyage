from django.contrib import admin

# Register your models here.
from .models import Excursion, Panorama

admin.site.register(Excursion)
admin.site.register(Panorama)