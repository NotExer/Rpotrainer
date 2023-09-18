from apps.cliente.views import clienteListView, clienteCreateView, clienteUpdateView, clienteDeleteView, cliente_inactivar
from django.urls import path

urlpatterns = [
    path('cliente/', clienteListView.as_view(), name='lista_cliente'),
    path('cliente/crear/', clienteCreateView.as_view(), name='crear_cliente'),
    path('cliente/<int:pk>/editar/', clienteUpdateView.as_view(), name='editar_cliente'),
    path('cliente/<int:pk>/eliminar/', clienteDeleteView.as_view(), name='eliminar_cliente'),
    path('cliente/<int:pk>/inactivar/', cliente_inactivar, name='inactivar_cliente')
]