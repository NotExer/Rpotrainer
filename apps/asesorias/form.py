from django import forms
from apps.asesorias.models import asesorias

class asesoriasform(forms.ModelForm):
    class Meta:
        model=asesorias
        
        fields = [
            'Guia_Suplemento',
            'Nutricion',
            'Tarifa',
            'Duracion',
        ]
        
        labels= {
            'Guia_Suplemento':'Guia Suplemento',
            'Nutricion':'Nutricion',
            'Tarifa':'Tarifa',
            'Duracion':'Duracion',
        }
        widgets = {
            'Guia_Suplemento': forms.TextInput(attrs={'class': 'hola'}),
            'Nutricion': forms.NumberInput(attrs={'class': 'hola'}),
            'Tarifa': forms.NumberInput(attrs={'class': 'hola'}),
            'Duracion': forms.NumberInput(attrs={'class': 'hola'}),
        }