from rest_framework.test import APITestCase
from rest_framework import status
from usuarios.models import Usuario
from lugares.models import LugarTuristico

class RutasTest(APITestCase):
    def setUp(self):
        self.experto = Usuario.objects.create_user(email="exp@example.com", username="exp", password="pass123", rol="experto")
        self.normal = Usuario.objects.create_user(email="norm@example.com", username="norm", password="pass123", rol="normal")

        self.lugar1 = LugarTuristico.objects.create(
            nombre="L1", descripcion="desc", categoria="atraccion",
            direccion="X", latitud=4.5, longitud=-74.1
        )
        self.lugar2 = LugarTuristico.objects.create(
            nombre="L2", descripcion="desc", categoria="restaurante",
            direccion="Y", latitud=4.6, longitud=-74.2
        )

    def autenticar(self, user):
        self.client.force_authenticate(user=user)

    def test_experto_puede_crear_ruta(self):
        self.autenticar(self.experto)
        data = {
            "nombre": "Ruta Andina",
            "descripcion": "Hermosa ruta",
            "lugar_ids": [self.lugar1.id, self.lugar2.id]
        }
        response = self.client.post("/api/rutas/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_normal_no_puede_crear_ruta(self):
        self.autenticar(self.normal)
        data = {
            "nombre": "Ruta Prohibida",
            "descripcion": "No debería poder",
            "lugar_ids": [self.lugar1.id]
        }
        response = self.client.post("/api/rutas/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
