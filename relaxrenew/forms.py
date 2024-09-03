from django import forms
from .models import Masaje

class MasajeForm(forms.ModelForm):
    class Meta:
        model = Masaje
        fields = ('nombre', 'descripcion', 'precio', 'duracion')