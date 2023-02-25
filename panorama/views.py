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
def excursions(request):
    context = {}
    context['excursions'] = Excursion.objects.all()
    return render(request, 'excursions/excursions.html', context)
def excursion(request, excursion_id):
    context = {}
    context['panorams'] = Panorama.objects.filter(excursion=excursion_id)
    return render(request, 'panorams/panorams.html', context)
def home(request):
    context = {}
    return render(request, 'home/home.html', context)