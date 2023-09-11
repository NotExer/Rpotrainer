from django import forms
from apps.nutricion.models import nutricion

class nutricionform(forms.ModelForm):
    class Meta:
        model=nutricion     
        fields = [
            'dia',
            'hora',
            'tipo_comida',
            'alimento',
            'porcion',
            'evitar',
            'otras_recomendaciones',
            'ingesta_agua',
            'dia_trampa',
            'suplementos',
            'lista_compra',
            
        ]
        labels= {
            'dia':'Dia',
            'hora':'Hora',
            'tipo_comida':'Tipo De Comida',
            'alimento':'Alimento',
            'porcion':'Porcion',
            'evitar':'Alimentos a evitar',
            'otras_recomendaciones' : 'Otras Recomendaciones',
            'ingesta_agua':'Ingesta de agua',
            'dia_trampa' : 'Dia Trampa',
            'suplementos' : 'Guia Suplementos',
            'lista_compra' : 'Lista de compra'
        }
        widgets = {
            'dia': forms.TextInput(attrs={'class':'form-control'}),
            'hora': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_comida': forms.TextInput(attrs={'class': 'form-control'}),
            'alimento': forms.TextInput(attrs={'class': 'form-control'}),
            'porcion': forms.TextInput(attrs={'class': 'form-control'}),
            'evitar': forms.TextInput(attrs={'class': 'form-control'}),
            'otras_recomendaiones': forms.TextInput(attrs={'class': 'form-control'}),
            'ingesta_agua': forms.TextInput(attrs={'class': 'form-control'}),
            'dia_trampa': forms.TextInput(attrs={'class': 'form-control'}),
            'suplementos': forms.TextInput(attrs={'class': 'form-control'}),
            'lista_compra': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
