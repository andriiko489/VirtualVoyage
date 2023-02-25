from django.urls import path, include
from .views import panorama, excursion, excursions
urlpatterns = [
    path('', excursions),
    path('<int:excursion_id>/', excursion),
    path('<int:excursion_id>/<int:panorama_id>/', panorama),
]