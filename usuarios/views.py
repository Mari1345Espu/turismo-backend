from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Usuario
from .serializers import UsuarioSerializer
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class PerfilUsuarioView(generics.RetrieveUpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user



@csrf_exempt
def crear_usuarios_demo(request):
    User = get_user_model()

    usuarios = [
        {"username": "admin", "email": "admin@demo.com", "password": "admin1234", "rol": "admin"},
        {"username": "experto", "email": "experto@demo.com", "password": "experto1234", "rol": "experto"},
        {"username": "normal", "email": "normal@demo.com", "password": "normal1234", "rol": "normal"},
    ]

    creados = []
    for u in usuarios:
        if not User.objects.filter(email=u["email"]).exists():
            User.objects.create_user(
                username=u["username"],
                email=u["email"],
                password=u["password"],
                rol=u["rol"]
            )
            creados.append(u["email"])

    return JsonResponse({"usuarios_creados": creados})
