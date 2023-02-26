from django.forms import ModelForm

from panorama.models import Panorama

class PaymentForm(ModelForm):
    class Meta:
        model = Panorama
        exclude = ('id','excursion')