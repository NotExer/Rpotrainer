from django.shortcuts import render
from apps.nutricion.models import nutricion
from apps.nutricion.form import nutricionform
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class nutricionListView(LoginRequiredMixin,ListView):
    model = nutricion
    template_name = 'nutricion/lista_nutricion.html'
    context_object_name = 'obj'
    paginate_by = 5
    login_url="iniciar"

class nutricionCreateView(CreateView):
    model = nutricion
    form_class = nutricionform
    template_name = 'nutricion/crear_nutricion.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('lista_nutricion')

class nutricionUpdateView(UpdateView):
    model = nutricion
    form_class = nutricionform
    template_name = 'nutricion/editar_nutricion.html'
    success_url = reverse_lazy('lista_nutricion')
    context_object_name = 'obj'

class nutricionDeleteView(DeleteView):
    model = nutricion
    template_name = 'nutricion/eliminar_nutricion.html'
    success_url = reverse_lazy('lista_nutricion')
    context_object_name = 'obj'