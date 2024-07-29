from django import forms
from .models import Evento


class ProductForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
