from django import forms
from apps.entrenamiento.models import entrenamiento

class entrenamientoform(forms.ModelForm):
    class Meta:
        model=entrenamiento     
        fields = [
            'Tipo',
            'Lista_Ejercicios',
            'Tarifa',
            'Modalidad',
            'Duracion',
        ]
        labels= {
            'Tipo':'Tipo',
            'Lista_Ejercicios':'Lista Ejercicios',
            'Tarifa':'Tarifa',
            'Modalidad':'Modalidad',
            'Duracion':'Duración',
        }
        widgets={
            'Tipo': forms.TextInput(attrs={'class':'form-control'}),
            'Lista_Ejercicios': forms.TextInput(attrs={'class':'form-control'}),
            'Tarifa': forms.NumberInput(attrs={'class':'form-control'}),
            'Modalidad': forms.TextInput(attrs={'class':'form-control'}),
            'Duracion': forms.TextInput(attrs={'class':'form-control'}),
        }