from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from panorama.views import panorama
urlpatterns = [
    path('panorama/<int:excursion_id>/<int:panorama_id>/', panorama),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)