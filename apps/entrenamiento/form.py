from django import forms
from apps.entrenamiento.models import entrenamiento

class entrenamientoform(forms.ModelForm):
    class Meta:
        model=entrenamiento     
        fields = [
            'musculo',
            'ejercicio',
            'series',
            'repeticiones',
            'rir',
            'cadencia',
            'microPausa',
            'macroPausa',
            'descripcion',
            'imagen',
        ]
        labels= {
            'musculo':'Músculo',
            'ejercicio':'Ejercicio',
            'series':'Series',
            'repeticiones':'Repeticiones',
            'rir':'Rir (Repeticiones en recamara)',
            'cadencia':'Cadencia',
            'microPausa':'Micro Pausa (min)',
            'macroPausa':'Macro Pausa (min)',
            'descripcion': 'Descripción',
            'imagen':'Imagen'
        }
        widgets={
            'musculo': forms.TextInput(attrs={'class':'form-control'}),
            'ejercicio': forms.TextInput(attrs={'class':'form-control'}),
            'series': forms.NumberInput(attrs={'class':'form-control'}),
            'repeticiones': forms.NumberInput(attrs={'class':'form-control'}),
            'rir': forms.NumberInput(attrs={'class':'form-control'}),
            'cadencia': forms.NumberInput(attrs={'class':'form-control'}),
            'microPausa': forms.NumberInput(attrs={'class':'form-control'}),
            'macroPausa': forms.NumberInput(attrs={'class':'form-control'}),
            'descripción': forms.TextInput(attrs={'class':'form-control'}),
            'imagen': forms.TextInput(attrs={'class':'form-control'}),
        }