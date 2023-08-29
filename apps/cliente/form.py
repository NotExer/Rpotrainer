from django import forms
from apps.cliente.models import cliente

class clienteform(forms.ModelForm):

    class Meta:
        model=cliente
        fields = [
            'Nombre',
            'Apellidos',
            'Edad',
            'Telefono',
            'Email',
            'Domicilio',
        ]
        labels= {
            'Nombre':'Nombre',
            'Apellidos':'Apellidos',
            'Edad':'Edad',
            'Telefono':'Telefono',
            'Email':'Email',
            'Domicilio':'Domicilio',
        }
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'Edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'Telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Domicilio': forms.Textarea(attrs={'class': 'form-contrl'}),
        }
