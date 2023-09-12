from django.shortcuts import render
from apps.medidas.models import medidas
from apps.medidas.form import medidasform
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class medidasListView(LoginRequiredMixin, ListView):
    model = medidas
    template_name = 'medidas/lista_medidas.html'
    context_object_name = 'obj'
    paginate_by = 5
    login_url="iniciar"

class medidasCreateView(CreateView):
    model = medidas
    form_class = medidasform
    template_name = 'medidas/crear_medidas.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('lista_medidas')
        

class medidasUpdateView(UpdateView):
    model = medidas
    form_class = medidasform
    template_name = 'medidas/editar_medidas.html'
    success_url = reverse_lazy('lista_medidas')
    context_object_name = 'obj'

class medidasDeleteView(DeleteView):
    model = medidas
    template_name = 'medidas/eliminar_medidas.html'
    success_url = reverse_lazy('lista_medidas')
    context_object_name = 'obj'