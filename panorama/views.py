from django.http import HttpResponse
from django.shortcuts import render

from .models import Panorama, Excursion
def panorama(request, excursion_id=0, panorama_id=0):
    print(excursion_id,panorama_id)
    print(Excursion.objects.get(id=excursion_id))
    panorama = Panorama.objects.filter(excursion=excursion_id)[panorama_id]
    context = {'panorama': panorama}
    return render(request, 'panorama/panorama.html', context);