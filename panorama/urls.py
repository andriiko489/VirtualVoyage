from django.urls import path, include, reverse
from .views import panorama, excursion, excursions, ExcursionCreateView, PanoramaCreateView
urlpatterns = [
    path('', excursions, name='excursions'),
    path('create/', ExcursionCreateView.as_view(success_url='/panorama/')),
    path('<int:excursion_id>/create/', PanoramaCreateView.as_view()),
    path('<int:excursion_id>/', excursion),
    path('<int:excursion_id>/<int:panorama_id>/', panorama),
]