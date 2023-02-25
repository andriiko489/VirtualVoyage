from django.urls import path, include
from .views import panorama, excursion
urlpatterns = [
    path('<int:excursion_id>/<int:panorama_id>/', panorama),
    path('', excursion),
]