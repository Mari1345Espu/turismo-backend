from django.urls import path
from .views import PerfilUsuarioView, crear_usuarios_demo

urlpatterns = [
    path('mi-perfil/', PerfilUsuarioView.as_view(), name='mi-perfil'),  
    path('crear-usuarios-demo/', crear_usuarios_demo),
]

