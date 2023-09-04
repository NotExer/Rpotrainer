from diagnostico.views import diagnosticoListView, diagnosticoCreateView, diagnosticoUpdateView, diagnosticoDeleteView
from django.urls import path

urlpatterns = [
    path('diagnostico/', diagnosticoListView.as_view(), name='lista_diagnostico'),
    path('diagnostico/crear/', diagnosticoCreateView.as_view(), name='crear_diagnostico'),
    path('diagnostico/<int:pk>/editar/', diagnosticoUpdateView.as_view(), name='editar_diagnostico'),
    path('diagnostico/<int:pk>/eliminar/', diagnosticoDeleteView.as_view(), name='eliminar_diagnostico'),
]