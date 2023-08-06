from apps.medidas.views import medidasListView, medidasCreateView, medidasUpdateView, medidasDeleteView
from django.urls import path, re_path

urlpatterns = [
    path('medidas/', medidasListView.as_view(), name='lista_medidas'),
    path('medidas/crear/', medidasCreateView.as_view(), name='crear_medidas'),
    path('medidas/<int:pk>/editar/', medidasUpdateView.as_view(), name='editar_medidas'),
    path('medidas/<int:pk>/eliminar/', medidasDeleteView.as_view(), name='eliminar_medidas'),
]


