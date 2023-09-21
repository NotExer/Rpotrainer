from apps.entrenamiento.views import entrenamientosListView, entrenamientoCreateView, entrenamientoUpdateView, entrenamientoDeleteView
from django.urls import path, re_path
from apps.entrenamiento.reportes import ReporteEntrenamiento

urlpatterns = [
    path('entrenamientos/', entrenamientosListView.as_view(), name='lista_entrenamientos'),
    path('entrenamientos/crear/', entrenamientoCreateView.as_view(), name='crear_entrenamiento'),
    path('entrenamientos/<int:pk>/editar/', entrenamientoUpdateView.as_view(), name='editar_entrenamiento'),
    path('entrenamientos/<int:pk>/eliminar/', entrenamientoDeleteView.as_view(), name='eliminar_entrenamiento'),
    path('entrenamientos/reporte', ReporteEntrenamiento, name='print_entrenamiento'),
]