from django.shortcuts import render
from apps.entrenador.models import entrenador
from apps.entrenador.form import entrenadorform
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class entrenadorListView(ListView):
    model = entrenador
    template_name = 'entrenador/lista_entrenador.html'
    context_object_name = 'obj'
    paginate_by = 5

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

class entrenadorDeleteView(DeleteView):
    model = entrenador
    template_name = 'entrenador/eliminar_entrenador.html'
    success_url = reverse_lazy('lista_entrenador')