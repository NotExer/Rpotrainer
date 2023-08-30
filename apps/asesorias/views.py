from django.shortcuts import render
from apps.asesorias.models import asesorias
from apps.asesorias.form import asesoriasform
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class asesoriasListView(ListView):
    model = asesorias
    template_name = 'asesorias/lista_asesorias.html'
    context_object_name = 'asesorias'
    paginate_by = 5

class asesoriasCreateView(CreateView):
    model = asesorias
    form_class = asesoriasform
    template_name = 'asesorias/crear_asesorias.html'
    success_url = reverse_lazy('lista_asesorias')

class asesoriasUpdateView(UpdateView):
    model = asesorias
    form_class = asesoriasform
    template_name = 'asesorias/editar_asesorias.html'
    success_url = reverse_lazy('lista_asesorias')

class asesoriasDeleteView(DeleteView):
    model = asesorias
    template_name = 'asesorias/eliminar_asesorias.html'
    success_url = reverse_lazy('lista_asesorias')
