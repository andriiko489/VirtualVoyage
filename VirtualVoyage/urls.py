from django.contrib import admin
from django.urls import path

from panorama.views import panorama
urlpatterns = [
    path('panorama/', panorama),
    path('admin/', admin.site.urls),
]
