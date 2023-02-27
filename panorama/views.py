from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User

from .models import Panorama, Excursion
from .form import PanoramaForm
def panorama(request, excursion_id=1, panorama_id=1):
    if (Excursion.objects.get(id=excursion_id).is_private == False) or (
            str(request.user) in map(str, Excursion.objects.get(id=excursion_id).users.all())):
        panorams = Panorama.objects.filter(excursion=excursion_id)
        num = len(panorams)
        panorama = panorams[panorama_id-1]
        context = {'panorama': panorama, "excursion_id":excursion_id, "panorama_id":panorama_id, 'num': num}
        return render(request, 'panorama/panorama.html', context)
    else:
        raise PermissionDenied
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
        raise PermissionDenied
def home(request):
    context = {}
    return render(request, 'home/home.html', context)
@method_decorator([login_required], name = 'dispatch')
class ExcursionCreateView(CreateView):
    model = Excursion
    fields = ['title','image','is_private','users']
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('excursions')
    #def get_context_data(self, **kwargs):
    #    # Call the base implementation first to get a context
    #    context = super().get_context_data(**kwargs)
    #    # Add in a QuerySet of all the books
    #    context['users'] = User.objects.all()
    #    return context
@method_decorator([login_required], name = 'dispatch')
class PanoramaCreateView(CreateView):
    form_class = PanoramaForm
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