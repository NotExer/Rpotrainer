from django import forms
from apps.entrenador.models import entrenador
from django.contrib.auth.forms import UserCreationForm

class entrenadorform(forms.ModelForm):
    class Meta:
        model=entrenador
        
        fields = [
            'nombre',
            'correo',
            'numero_contacto',
        ]
        
        labels= {
            'nombre': 'Nombre',
            'correo': 'Correo',
            'numero_contacto': 'Número de contacto',
        }
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'numero_contacto': forms.TextInput(attrs={'class': 'form-control'}),
        }