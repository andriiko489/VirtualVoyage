from django.forms import ModelForm

from panorama.models import Panorama
from django.contrib.auth.models import User

class PanoramaForm(ModelForm):
    USERS = User.objects.all()

    class Meta:
        model = Panorama
        exclude = ('id','excursion')