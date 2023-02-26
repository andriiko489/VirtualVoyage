from django.forms import ModelForm

from panorama.models import Panorama

class PanoramaForm(ModelForm):
    class Meta:
        model = Panorama
        exclude = ('id','excursion')