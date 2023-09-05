from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

    
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
            'username': forms.TextInput(attrs={'class':'form-style'}),
            'email': forms.EmailInput(attrs={'class':'form-style'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-style'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-style'}),
        } 
        help_texts = {
        'username': None,
        'email' : None,
    }
        
        