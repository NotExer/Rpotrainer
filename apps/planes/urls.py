from apps.planes.views import planesListView, planesCreateView, planesUpdateView, planesDeleteView
from django.urls import path
from apps.planes.reportes import ReportePlanes


urlpatterns = [
    path('planes/', planesListView.as_view(), name='lista_planes'),
    path('planes/crear/', planesCreateView.as_view(), name='crear_planes'),
    path('planes/<int:pk>/editar/', planesUpdateView.as_view(), name='editar_planes'),
    path('planes/reporte', ReportePlanes, name='print_planes'),
]