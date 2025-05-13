from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Usuario
from .serializers import UsuarioSerializer

# Create your views here.

class PerfilUsuarioView(generics.RetrieveUpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user