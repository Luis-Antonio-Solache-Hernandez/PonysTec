from django import forms
from .models import Producto, Puesto, Trabajador


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = ['id']
