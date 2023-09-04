from apps.asesorias.views import asesoriasListView, asesoriasCreateView, asesoriasUpdateView, asesoriasDeleteView
from django.urls import path

urlpatterns = [
    path('asesorias/', asesoriasListView.as_view(), name='lista_asesorias'),
    path('asesorias/crear/', asesoriasCreateView.as_view(), name='crear_asesorias'),
    path('asesorias/<int:pk>/editar/', asesoriasUpdateView.as_view(), name='editar_asesorias'),
    path('asesorias/<int:pk>/eliminar/', asesoriasDeleteView.as_view(), name='eliminar_asesorias'),
]