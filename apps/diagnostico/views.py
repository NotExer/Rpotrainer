from django.shortcuts import render
from apps.diagnostico.models import diagnostico
from apps.diagnostico.form import diagnosticoform
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class diagnosticoListView(LoginRequiredMixin, ListView):
    model = diagnostico
    template_name = 'diagnostico/lista_diagnostico.html'
    context_object_name = 'obj'
    paginate_by = 5
    login_url="iniciar"

class diagnosticoCreateView(CreateView):
    model = diagnostico
    form_class = diagnosticoform
    template_name = 'diagnostico/crear_diagnostico.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('lista_diagnostico')

class diagnosticoUpdateView(UpdateView):
    model = diagnostico
    form_class = diagnosticoform
    template_name = 'diagnostico/editar_diagnostico.html'
    success_url = reverse_lazy('lista_diagnostico')
    context_object_name = 'obj'

class diagnosticoDeleteView(DeleteView):
    model = diagnostico
    template_name = 'diagnostico/eliminar_diagnostico.html'
    success_url = reverse_lazy('lista_diagnostico')
    context_object_name = 'obj'