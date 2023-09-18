from django.shortcuts import render
from apps.entrenador.models import entrenador
from apps.entrenador.form import entrenadorform
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class entrenadorListView(LoginRequiredMixin, ListView):
    model = entrenador
    template_name = 'entrenador/lista_entrenador.html'
    context_object_name = 'obj'
    paginate_by = 5
    login_url="iniciar"

class entrenadorCreateView(CreateView):
    model = entrenador
    form_class = entrenadorform
    template_name = 'entrenador/crear_entrenador.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('lista_entrenador')

class entrenadorUpdateView(UpdateView):
    model = entrenador
    form_class = entrenadorform
    template_name = 'entrenador/editar_entrenador.html'
    success_url = reverse_lazy('lista_entrenador')
    context_object_name = 'obj'
    
    
class entrenadorDeleteView(UpdateView):
    model = entrenador
    form_class = entrenadorform
    template_name = 'entrenador/eliminar_entrenador.html'
    success_url = reverse_lazy('lista_entrenador')
    context_object_name = 'obj'