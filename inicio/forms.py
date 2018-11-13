from django import forms
from .models import Persona

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('nombre', 'email', 'rut', 'contrasena', 'nacimiento' , 'region' , 'comuna' , 'telefono' , 'suscripcion' , )