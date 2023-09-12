from apps.planes.views import planesListView, planesCreateView, planesUpdateView, planesDeleteView
from django.urls import path

urlpatterns = [
    path('planes/', planesListView.as_view(), name='lista_planes'),
    path('planes/crear/', planesCreateView.as_view(), name='crear_planes'),
    path('planes/<int:pk>/editar/', planesUpdateView.as_view(), name='editar_planes'),
    path('planes/<int:pk>/eliminar/', planesDeleteView.as_view(), name='eliminar_planes'),
]