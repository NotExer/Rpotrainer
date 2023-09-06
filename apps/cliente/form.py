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
            'Edad',
            'Telefono',
            'Email',
            'Domicilio',

        ]
        labels= {
            'NombreCompleto':'Nombre Completo',
            'FechaInicio':'Fecha de inicio',
            'Fecha Fin':'Fecha de finalización',
            'FechaPago':'Fecha de pago',
            'Edad': 'Edad',
            'Telefono':'Telefono',
            'Email':'Email',
            'Domicilio': 'Domicilio',
            
        }
        widgets = {
            'NombreCompleto': forms.TextInput(attrs={'class': 'form-control'}),
            'FechaInicio': forms.DateInput(attrs={'class': 'form-control'}),
            'FechaFin': forms.DateInput(attrs={'class': 'form-control'}),
            'FechaPago': forms.DateInput(attrs={'class': 'form-control'}),
            'Edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'Telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Domicilio': forms.Textarea(attrs={'class': 'form-contrl'}),
            
        }
