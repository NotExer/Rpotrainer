from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from apps.registro.models import Perfil


        
    
class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        labels= {
            'username':'Nombre',
            'email':'Correo',
            'password1':'Contraseña',
            'password2':'Verificar contraseña',
        }
        
        widgets = {
            'username': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.NumberInput(attrs={'class':'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }    