from django import forms
from apps.entrenador.models import entrenador
from django.contrib.auth.forms import UserCreationForm

class entrenadorform(forms.ModelForm):
    class Meta:
        model=entrenador
        
        fields = [
            'nombre',
            'apellido',
            'correo',
            'numero_contacto',
        ]
        
        labels= {
            'nombre': 'nombre',
            'apellido': 'apellido',
            'correo': 'correo',
            'numero_contacto': 'numero de contacto',
        }
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'numero_contacto': forms.TextInput(attrs={'class': 'form-control'}),
        }