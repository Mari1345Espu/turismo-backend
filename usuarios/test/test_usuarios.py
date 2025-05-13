from rest_framework.test import APITestCase
from rest_framework import status
from usuarios.models import Usuario

class UsuarioTest(APITestCase):

    def test_registro_usuario(self):
        data = {
            "email": "nuevo@example.com",
            "username": "nuevo",
            "password": "Test1234!",
            "re_password": "Test1234!",
            "rol": "normal"
        }
        response = self.client.post("/auth/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Usuario.objects.count(), 1)

    def test_login_usuario(self):
        user = Usuario.objects.create_user(email="login@example.com", username="login", password="Test1234")
        data = {
            "email": "login@example.com",
            "password": "Test1234"
        }
        response = self.client.post("/auth/jwt/create/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_obtener_perfil(self):
        user = Usuario.objects.create_user(email="perfil@example.com", username="perfil", password="Test1234")
        self.client.force_authenticate(user=user)
        response = self.client.get("/auth/users/me/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], "perfil@example.com")

    def test_editar_perfil(self):
        user = Usuario.objects.create_user(email="editar@example.com", username="viejo", password="Test1234")
        self.client.force_authenticate(user=user)
        data = {"username": "nuevo"}
        response = self.client.put("/usuarios/mi-perfil/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "nuevo")

    def test_cambiar_contraseña(self):
        user = Usuario.objects.create_user(email="clave@example.com", username="clave", password="OldPass123")
        self.client.force_authenticate(user=user)
        data = {
            "current_password": "OldPass123",
            "new_password": "NewPass123"
        }
        response = self.client.post("/auth/users/set_password/", data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_login_con_password_incorrecto(self):
        Usuario.objects.create_user(email="fail@example.com", username="fail", password="Correcto123")
        data = {
            "email": "fail@example.com",
            "password": "Incorrecto"
        }
        response = self.client.post("/auth/jwt/create/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_registro_con_passwords_diferentes(self):
        data = {
            "email": "error@example.com",
            "username": "error",
            "password": "Uno12345",
            "re_password": "Dos12345",
            "rol": "normal"
        }
        response = self.client.post("/auth/users/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("non_field_errors", response.data)

        
    def test_solicitud_recuperacion_password(self):
        Usuario.objects.create_user(email="recuperar@example.com", username="recuperar", password="Recup123")
        data = {"email": "recuperar@example.com"}
        response = self.client.post("/auth/users/reset_password/", data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

