from django import forms
from apps.planes.models import planes

class planesform(forms.ModelForm):

    class Meta:
        model=planes
        fields = [
            'nombre',
            'tarifa',
            'descuento',
            'total',
            'fechainicio',
            'fechafin',
            'modalidad',


        ]
        labels= {
            'nombre':'Nombre Completo',
            'tarifa':'Tarifa',
            'descuento': 'Descuento',
            'total': 'Total',
            'fechainicio':'Fecha de inicio',
            'fechafin':'Fecha de finalización',
            'modalidad': 'Modalidad',

            
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tarifa': forms.NumberInput(attrs={'class': 'form-control'}),
            'descuento': forms.NumberInput(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'fechainicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fechafin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'modalidad': forms.TextInput(attrs={'class': 'form-control'}),
        }