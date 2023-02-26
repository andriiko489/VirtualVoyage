from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Panorama, Excursion
from .form import PaymentForm
def panorama(request, excursion_id=1, panorama_id=1):
    if (Excursion.objects.get(id=excursion_id).is_private == False) or (
            str(request.user) in map(str, Excursion.objects.get(id=excursion_id).users.all())):
        print(excursion_id)
        panorams = Panorama.objects.filter(excursion=excursion_id)
        num = len(panorams)
        panorama = panorams[panorama_id-1]
        context = {'panorama': panorama, "excursion_id":excursion_id, "panorama_id":panorama_id, 'num': num}
        return render(request, 'panorama/panorama.html', context)
    else:
        return HttpResponse("405 Error: У вас немає доступу")
def excursions(request):
    context = {}
    context['excursions'] = Excursion.objects.filter(is_private=False)
    return render(request, 'excursions/excursions.html', context)
def excursion(request, excursion_id):
    if (Excursion.objects.get(id=excursion_id).is_private==False) or (str(request.user) in map(str, Excursion.objects.get(id=excursion_id).users.all())):
        context = {}
        context['panorams'] = Panorama.objects.filter(excursion=excursion_id)
        return render(request, 'panorams/panorams.html', context)
    else:
        return HttpResponse("405 Error: У вас немає доступу")
def home(request):
    context = {}
    return render(request, 'home/home.html', context)

class ExcursionCreateView(CreateView):
    model = Excursion
    fields = ['title','description','image','is_private','users']
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('excursions')
class PanoramaCreateView(CreateView):
    form_class = PaymentForm
    template_name = "panorama/panorama_form.html"
    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        self.object.excursion = Excursion.objects.get(id=self.kwargs.get('excursion_id'))

        super(PanoramaCreateView, self).form_valid(form)
        return super().form_valid(form)
    def post(self, request, excursion_id, *args, **kwargs):
        self.excursion = excursion_id
        return super().post(request, *args, **kwargs)
    def get_success_url(self):
        return "/panorama/"+str(self.kwargs.get('excursion_id'))