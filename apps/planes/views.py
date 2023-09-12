from django.shortcuts import render
from apps.planes.models import planes
from apps.planes.form import planesform
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



class planesListView(LoginRequiredMixin, ListView, ):
    model = planes
    template_name = 'planes/lista_planes.html'
    context_object_name = 'obj'
    paginate_by = 5
    login_url="iniciar"
    

class planesCreateView(CreateView):
    model = planes
    form_class = planesform
    template_name = 'cliente/crear_planes.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('lista_planes')

class planesUpdateView(UpdateView):
    model = planes
    form_class = planesform
    template_name = 'planes/editar_planes.html'
    success_url = reverse_lazy('lista_planes')
    context_object_name = 'obj'

class planesDeleteView(DeleteView):
    model = planes
    template_name = 'planes/eliminar_planes.html'
    success_url = reverse_lazy('lista_planes')
    context_object_name = 'obj'
    
    
    


