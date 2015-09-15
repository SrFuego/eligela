# Python imports


# Django imports
from django import forms


# Local imports
from .models import Colegio


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Colegio
        fields = ('nombre', 'distrito', 'telefono', 'direccion', 'asunto',)
