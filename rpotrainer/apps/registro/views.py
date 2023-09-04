from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from apps.registro.models import Perfil
from apps.registro.forms import CustomUserForm



def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid(): 
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.changed_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='cliente')
    return render(request, 'session/registro.html', data)




class LogInView(LoginView):
    template_name = 'session/iniciar.html'

class LogOutView(LogoutView):
    pass
