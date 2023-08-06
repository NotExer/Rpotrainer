from apps.entrenador.views import entrenadorListView, entrenadorCreateView, entrenadorUpdateView, entrenadorDeleteView
from django.urls import path

urlpatterns = [
    path('entrenador/', entrenadorListView.as_view(), name='lista_entrenador'),
    path('entrenador/crear/', entrenadorCreateView.as_view(), name='crear_entrenador'),
    path('entrenador/<int:pk>/editar/', entrenadorUpdateView.as_view(), name='editar_entrenador'),
    path('entrenador/<int:pk>/eliminar/', entrenadorDeleteView.as_view(), name='eliminar_entrenador'),
]