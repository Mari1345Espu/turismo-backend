from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import LugarTuristico, ComentarioLugar, RutaSugerida, Favorito
from math import radians, cos, sin, asin, sqrt
from .serializers import LugarTuristicoSerializer, ComentarioLugarSerializer, RutaSugeridaSerializer, FavoritoSerializer
from .permissions import EsExpertoOAdmin, EsDueñoOAdmin
def calcular_distancia(lat1, lon1, lat2, lon2):
    # Fórmula de Haversine
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radio de la Tierra en km
    return c * r

class LugarTuristicoViewSet(viewsets.ModelViewSet):
    queryset = LugarTuristico.objects.all()
    serializer_class = LugarTuristicoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['categoria']  # Filtrar por categoría
    ordering_fields = ['calificacion_promedio', 'nombre']  # ⭐ orden por calificación o nombre
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [EsExpertoOAdmin()]
        return [permissions.AllowAny()] 
    
    def list(self, request, *args, **kwargs):
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')

        queryset = self.get_queryset()

        if lat and lon:
            lat = float(lat)
            lon = float(lon)
            queryset = sorted(
                queryset,
                key=lambda lugar: calcular_distancia(lat, lon, float(lugar.latitud), float(lugar.longitud))
            )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ComentarioLugarViewSet(viewsets.ModelViewSet):
    queryset = ComentarioLugar.objects.all().order_by('-fecha')
    serializer_class = ComentarioLugarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [EsDueñoOAdmin()]
        elif self.action == 'create':
            return [EsExpertoOAdmin()]
        return [permissions.AllowAny()]
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class RutaSugeridaViewSet(viewsets.ModelViewSet):
    queryset = RutaSugerida.objects.all()
    serializer_class = RutaSugeridaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [EsExpertoOAdmin()]
        return [permissions.AllowAny()]
    
class FavoritoViewSet(viewsets.ModelViewSet):
    serializer_class = FavoritoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorito.objects.filter(usuario=self.request.user)
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [EsDueñoOAdmin()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)