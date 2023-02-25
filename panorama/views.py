from django.http import HttpResponse
from django.shortcuts import render

from .models import Panorama, Excursion
def panorama(request, excursion_id=0, panorama_id=0):
    print(excursion_id)
    panorams = Panorama.objects.filter(excursion=excursion_id)
    num = len(panorams)
    panorama = panorams[panorama_id]
    context = {'panorama': panorama, "excursion_id":excursion_id, "panorama_id":panorama_id, 'num': num}
    return render(request, 'panorama/panorama.html', context)

def excursion(request):
    context = {}
    context['excursions'] = Excursion.objects.all()
    print(context['excursions'][0].image.url)
    return render(request, 'tour/tour.html', context)