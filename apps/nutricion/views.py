from django.shortcuts import render
from apps.nutricion.models import nutricion
from apps.nutricion.form import nutricionform
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class nutricionListView(ListView):
    model = nutricion
    template_name = 'nutricion/lista_nutricion.html'
    context_object_name = 'nutricion'
    paginate_by = 5

class nutricionCreateView(CreateView):
    model = nutricion
    form_class = nutricionform
    template_name = 'nutricion/crear_nutricion.html'
    success_url = reverse_lazy('lista_nutricion')

class nutricionUpdateView(UpdateView):
    model = nutricion
    form_class = nutricionform
    template_name = 'nutricion/editar_nutricion.html'
    success_url = reverse_lazy('lista_nutricion')

class nutricionDeleteView(DeleteView):
    model = nutricion
    template_name = 'nutricion/eliminar_nutricion.html'
    success_url = reverse_lazy('lista_nutricion')