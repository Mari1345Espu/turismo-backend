from rest_framework.test import APITestCase
from rest_framework import status
from usuarios.models import Usuario
from lugares.models import LugarTuristico, Favorito

class FavoritosTest(APITestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(email="user@example.com", username="user", password="pass123")
        self.otro = Usuario.objects.create_user(email="otro@example.com", username="otro", password="pass123")

        self.lugar = LugarTuristico.objects.create(
            nombre="Sitio X", descripcion="desc", categoria="atraccion",
            direccion="X", latitud=4.5, longitud=-74.1
        )

        self.fav = Favorito.objects.create(usuario=self.otro, lugar=self.lugar)

    def autenticar(self, user):
        self.client.force_authenticate(user=user)

    def test_usuario_puede_guardar_favorito(self):
        self.autenticar(self.user)
        data = {"lugar": self.lugar.id}
        response = self.client.post("/api/favoritos/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_usuario_no_puede_eliminar_favorito_de_otro(self):
        self.autenticar(self.user)
        response = self.client.delete(f"/api/favoritos/{self.fav.id}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

