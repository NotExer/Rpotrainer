from django.shortcuts import render
from apps.cliente.models import cliente
from apps.cliente.form import clienteform
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render


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
    cliente=cliente.objects.filter(pk=id).first()
    contexto={}
    template_name="cliente/inactivar_cliente.html"
    if not cliente:
        return redirect("listar_cliente")
    
    if request.method=='GET':
        context={'obj':cliente}
    
    if request.method=='POST':
        cliente.estado=False
        cliente.save()
        return redirect("listar_cliente")
    
    
    


