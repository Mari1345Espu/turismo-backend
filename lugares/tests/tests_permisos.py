from django.test import TestCase

# Create your tests here.

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from usuarios.models import Usuario
from lugares.models import LugarTuristico, ComentarioLugar

class PermisosTest(APITestCase):

    def setUp(self):
        self.usuario_normal = Usuario.objects.create_user(
            email="normal@example.com", username="normal", password="test1234", rol="normal"
        )
        self.usuario_experto = Usuario.objects.create_user(
            email="experto@example.com", username="experto", password="test1234", rol="experto"
        )

    def autenticar(self, usuario):
        self.client.force_authenticate(user=usuario)

    def test_usuario_normal_no_puede_crear_lugar(self):
        self.autenticar(self.usuario_normal)
        data = {
            "nombre": "Cascada Secreta",
            "descripcion": "Una cascada oculta",
            "categoria": "atraccion",
            "direccion": "Montañas",
            "latitud": 4.5,
            "longitud": -74.1
        }
        response = self.client.post("/api/lugares/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_experto_puede_crear_lugar(self):
        self.autenticar(self.usuario_experto)
        data = {
            "nombre": "Mirador del Cielo",
            "descripcion": "Vista panorámica",
            "categoria": "atraccion",
            "direccion": "Colina Alta",
            "latitud": 4.6,
            "longitud": -74.2
        }
        response = self.client.post("/api/lugares/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_usuario_no_puede_borrar_comentario_ajeno(self):
        lugar = LugarTuristico.objects.create(
            nombre="Sitio 1", descripcion="X", categoria="atraccion",
            direccion="Y", latitud=4.7, longitud=-74.3
        )
        otro_usuario = Usuario.objects.create_user(
            email="otro@example.com", username="otro", password="test1234"
        )
        comentario = ComentarioLugar.objects.create(
            lugar=lugar, usuario=otro_usuario, texto="Muy bonito", calificacion=5
        )
        self.autenticar(self.usuario_normal)
        url = f"/api/comentarios/{comentario.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

