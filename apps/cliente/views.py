from django.shortcuts import render
from apps.cliente.models import cliente
from apps.cliente.form import clienteform
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.http import HttpResponse
import json


class clienteListView(LoginRequiredMixin, ListView, ):
    model = cliente
    template_name = 'cliente/lista_cliente.html'
    context_object_name = 'obj'
    paginate_by = 5
    login_url="iniciar"
    

class clienteCreateView(CreateView):
    model = cliente
    form_class = clienteform
    template_name = 'cliente/crear_cliente.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('lista_cliente')

class clienteUpdateView(UpdateView):
    model = cliente
    form_class = clienteform
    template_name = 'cliente/editar_cliente.html'
    success_url = reverse_lazy('lista_cliente')
    context_object_name = 'obj'

class clienteDeleteView(DeleteView):
    model = cliente
    template_name = 'cliente/eliminar_cliente.html'
    success_url = reverse_lazy('lista_cliente')
    context_object_name = 'obj'
    
    
    
    
    
    
def cliente_inactivar(request, id):
    template_name="inactivar_cliente.html"
    contexto={}
    Cliente=cliente.objects.filter(pk=id).first()
    if not Cliente:
        return HttpResponse('Cliente no existe' + str(id))
    if request.method=='GET':
        contexto={'obj':Cliente}
    if request.method=='POST':
        Cliente.estado=False
        Cliente.save()
        contexto={'obj':'OK'}
        return HttpResponse('Cliente inactivado')
    return render(request, template_name, contexto)
    
    
    


