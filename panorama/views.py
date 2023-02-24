from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse('''''')
def panorama(request):
    context={}
    return render(request, 'panorama/panorama.html', context);