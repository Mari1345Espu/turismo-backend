from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LugarTuristicoViewSet, ComentarioLugarViewSet, RutaSugeridaViewSet, FavoritoViewSet

router = DefaultRouter()
router.register(r'lugares', LugarTuristicoViewSet)
router.register(r'comentarios', ComentarioLugarViewSet)
router.register(r'rutas', RutaSugeridaViewSet)
router.register(r'favoritos', FavoritoViewSet, basename='favorito')

urlpatterns = [
    path('', include(router.urls)),
]
