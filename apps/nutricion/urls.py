from nutricion.views import nutricionListView, nutricionCreateView, nutricionUpdateView, nutricionDeleteView
from django.urls import path
from apps.nutricion.reportes import ReporteNutricion

urlpatterns = [
    path('nutricion/', nutricionListView.as_view(), name='lista_nutricion'),
    path('nutricion/crear/', nutricionCreateView.as_view(), name='crear_nutricion'),
    path('nutricion/editar<int:pk>/editar/', nutricionUpdateView.as_view(), name='editar_nutricion'),
    path('nutricion/eliminar<int:pk>/eliminar/', nutricionDeleteView.as_view(), name='eliminar_nutricion'),
    path('nutricion/reporte', ReporteNutricion, name='print_nutricion'),
]