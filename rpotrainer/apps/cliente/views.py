from django.shortcuts import render
from apps.cliente.models import cliente
from apps.cliente.form import clienteform
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def Home(request):
    return render(request, "index/index")


class clienteListView(ListView):
    model = cliente
    template_name = 'cliente/lista_cliente.html'
    context_object_name = 'obj'
    paginate_by = 5
    

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

class clienteDeleteView(DeleteView):
    model = cliente
    template_name = 'cliente/eliminar_cliente.html'
    success_url = reverse_lazy('lista_cliente')


