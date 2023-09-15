from django import forms
from apps.cliente.models import cliente

class clienteform(forms.ModelForm):

    class Meta:
        model=cliente
        fields = [
            'NombreCompleto',
            'FechaInicio',
            'FechaFin',
            'FechaPago',

        ]
        labels= {
            'NombreCompleto':'Nombre Completo',
            'FechaInicio':'Fecha de inicio',
            'Fecha Fin':'Fecha de finalización',
            'FechaPago':'Fecha de pago',
        }
        widgets = {
            'NombreCompleto': forms.TextInput(attrs={'class': 'form-control'}),
            'FechaInicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'FechaFin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'FechaPago': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
