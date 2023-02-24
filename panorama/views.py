from django.http import HttpResponse
from django.shortcuts import render

from .models import Panorama, Excursion
def panorama(request, excursion_id=0, panorama_id=0):
    #excursion_id = 1
    panorams = Panorama.objects.filter(excursion=excursion_id)
    num = len(panorams)
    panorama = panorams[panorama_id]
    context = {'panorama': panorama, "excursion_id":excursion_id, "panorama_id":panorama_id, 'num': num}
    return render(request, 'panorama/panorama.html', context);