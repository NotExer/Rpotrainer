from django.contrib import admin
from django.urls import path, re_path, include
from apps.entrenamiento.views import entrenamientosListView, entrenamientoCreateView, entrenamientoUpdateView, entrenamientoDeleteView
from apps.medidas.views import medidasListView, medidasCreateView, medidasUpdateView, medidasDeleteView
from apps.nutricion.views import nutricionListView, nutricionCreateView, nutricionUpdateView, nutricionDeleteView
from apps.entrenador.views import entrenadorListView, entrenadorCreateView, entrenadorUpdateView, entrenadorDeleteView
from apps.diagnostico.views import diagnosticoListView, diagnosticoCreateView, diagnosticoUpdateView, diagnosticoDeleteView
from apps.cliente.views import clienteListView, clienteCreateView, clienteUpdateView, clienteDeleteView
from apps.asesorias.views import asesoriasListView, asesoriasCreateView, asesoriasUpdateView, asesoriasDeleteView
from apps.registro.views import CustomUserForm, LogInView, LogOutView, registro_usuario
from apps.Home.views import Home, entrenamiento_main, asesorias_main, nutricion_main, sobre_main, testimonios_main, contacto_main


urlpatterns = [
    re_path(r'^$', Home, name='Home'),
    re_path(r'^entrenamientoInfo$', entrenamiento_main, name='entrenamiento_main'),
    re_path(r'^asesoriasInfo$', asesorias_main, name='asesorias_main'),
    re_path(r'^nutricionInfo$', nutricion_main, name='nutricion_main'),
    re_path(r'^sobre$', sobre_main, name='sobre_main'),
    re_path(r'^testimonios$', testimonios_main, name='testimonios_main'),
    re_path(r'^contacto$', contacto_main, name='contacto_main'),    
    path('admin/', admin.site.urls),
    path('entrenamientos/', entrenamientosListView.as_view(), name='lista_entrenamientos'),
    path('entrenamientos/crear/', entrenamientoCreateView.as_view(), name='crear_entrenamiento'),
    path('entrenamientos/<int:pk>/editar/', entrenamientoUpdateView.as_view(), name='editar_entrenamiento'),
    path('entrenamientos/<int:pk>/eliminar/', entrenamientoDeleteView.as_view(), name='eliminar_entrenamiento'),
    path('medidas/', medidasListView.as_view(), name='lista_medidas'),
    path('medidas/crear/', medidasCreateView.as_view(), name='crear_medidas'),
    path('medidas/<int:pk>/editar/', medidasUpdateView.as_view(), name='editar_medidas'),
    path('medidas/<int:pk>/eliminar/', medidasDeleteView.as_view(), name='eliminar_medidas'),
    path('nutricion/', nutricionListView.as_view(), name='lista_nutricion'),
    path('nutricion/crear/', nutricionCreateView.as_view(), name='crear_nutricion'),
    path('nutricion/<int:pk>/editar/', nutricionUpdateView.as_view(), name='editar_nutricion'),
    path('nutricion/<int:pk>/eliminar/', nutricionDeleteView.as_view(), name='eliminar_nutricion'),
    path('entrenador/', entrenadorListView.as_view(), name='lista_entrenador'),
    path('entrenador/crear/', entrenadorCreateView.as_view(), name='crear_entrenador'),
    path('entrenador/<int:pk>/editar/', entrenadorUpdateView.as_view(), name='editar_entrenador'),
    path('entrenador/<int:pk>/eliminar/', entrenadorDeleteView.as_view(), name='eliminar_entrenador'),
    path('diagnostico/', diagnosticoListView.as_view(), name='lista_diagnostico'),
    path('diagnostico/crear/', diagnosticoCreateView.as_view(), name='crear_diagnostico'),
    path('diagnostico/<int:pk>/editar/', diagnosticoUpdateView.as_view(), name='editar_diagnostico'),
    path('diagnostico/<int:pk>/eliminar/', diagnosticoDeleteView.as_view(), name='eliminar_diagnostico'),
    path('cliente/', clienteListView.as_view(), name='lista_cliente'),
    path('cliente/crear/', clienteCreateView.as_view(), name='crear_cliente'),
    path('cliente/<int:pk>/editar/', clienteUpdateView.as_view(), name='editar_cliente'),
    path('cliente/<int:pk>/eliminar/', clienteDeleteView.as_view(), name='eliminar_cliente'),
    path('asesorias/', asesoriasListView.as_view(), name='lista_asesorias'),
    path('asesorias/crear/', asesoriasCreateView.as_view(), name='crear_asesorias'),
    path('asesorias/<int:pk>/editar/', asesoriasUpdateView.as_view(), name='editar_asesorias'),
    path('asesorias/<int:pk>/eliminar/', asesoriasDeleteView.as_view(), name='eliminar_asesorias'),
    path('incia-sesion/', LogInView.as_view(), name='iniciar'),
    path('registro/', registro_usuario, name='registro_usuario'), 
    path('cerrar-sesion/', LogOutView.as_view(), name='log-out'),
    path('accounts/', include ('django.contrib.auth.urls')),
]
