from django import forms
from apps.planes.models import planes

class planesform(forms.ModelForm):

    class Meta:
        model=planes
        fields = [
            'nombre',
            'tarifa',
            'fechainicio',
            'fechafin',
            'modalidad',


        ]
        labels= {
            'nombre':'Nombre Completo',
            'tarifa':'Tarifa',
            'fechainicio':'Fecha de inicio',
            'fechafin':'Fecha de finalización',
            'modalidad': 'Modalidad',

            
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tarifa': forms.FloatField(),
            'fechainicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fechafin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'modalidad': forms.TextInput(attrs={'class': 'form-control'}),
        }
