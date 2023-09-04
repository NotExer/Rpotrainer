from django import forms
from apps.entrenamiento.models import entrenamiento

class entrenamientoform(forms.ModelForm):
    class Meta:
        model=entrenamiento     
        fields = [
            'Musculo',
            'NombreEjercicio',
            'Repeticiones',
            'Series',
            'Rir',
            'MicroPausa',
            'MacroPausa',
            'Descripcion',
        ]
        labels= {
            'Musculo':'Musculo',
            'NombreEjercicio':'Nombre De Ejercicio',
            'Repeticiones':'Repeticiones',
            'Rir':'Rir',
            'MicroPausa':'MicroPausa',
            'MacroPausa':'MacroPausa',
            'Descripcion':'Descripcion',
        }
        widgets={
            
            
            'Musculo' : forms.TextInput(attrs={'class' : 'form-control'}),
            'NombreEjercicio' : forms.TextInput(attrs={'class' : 'form-control'}),
            'Repeticiones' : forms.TextInput(attrs={'class' : 'form-control'}),
            'Series' : forms.TextInput(attrs={'class' : 'form-control'}),
            'Rir' : forms.TextInput(attrs={'class' : 'form-control'}),
            'MicroPausa' : forms.TextInput(attrs={'class' : 'form-control'}),
            'MacroPausa' : forms.TextInput(attrs={'class' : 'form-control'}),
            'Descripcion' : forms.TextInput(attrs={'class' : 'form-control'}),
            
        }