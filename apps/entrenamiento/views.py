from apps.entrenamiento.models import entrenamiento
from apps.entrenamiento.form import entrenamientoform
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render


class entrenamientosListView(ListView):
    model = entrenamiento
    template_name = 'entrenamiento/lista_entrenamientos.html'
    context_object_name = 'obj'
    paginate_by = 5

class entrenamientoCreateView(CreateView):
    model = entrenamiento
    form_class = entrenamientoform
    template_name = 'entrenamiento/crear_entrenamiento.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('lista_entrenamientos')

class entrenamientoUpdateView(UpdateView):
    model = entrenamiento
    form_class = entrenamientoform
    template_name = 'entrenamiento/editar_entrenamiento.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('lista_entrenamientos')
    

class entrenamientoDeleteView(DeleteView):
    model = entrenamiento
    template_name = 'entrenamiento/eliminar_entrenamiento.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('lista_entrenamientos')