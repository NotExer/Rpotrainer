from django import forms
from apps.nutricion.models import nutricion

class nutricionform(forms.ModelForm):
    class Meta:
        model=nutricion     
        fields = [
            'Tarifa',
            'Duracion',
            'Guia_Alimentos',
            'Lista_Alimentos',
        ]
        labels= {
            'Tarifa':'Tarifa',
            'Duracion':'Duracion',
            'Guia_Alimentos':'Guia Alimentos',
            'Lista_Alimentos':'Lista Alimentos',
        }
        widgets = {
            'Tarifa': forms.NumberInput(attrs={'class':'form-control'}),
            'Duracion': forms.NumberInput(attrs={'class':'form-control'}),
            'Guia_Alimentos': forms.TextInput(attrs={'class': 'form-control'}),
            'Lista_Alimentos': forms.TextInput(attrs={'class': 'form-control'}),
        }