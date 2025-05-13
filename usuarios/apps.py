from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'

    def ready(self):
        from django.contrib.auth import get_user_model
        User = get_user_model()

        usuarios = [
            {"email": "usuario@example.com", "username": "normal", "rol": "normal"},
            {"email": "experto@example.com", "username": "experto", "rol": "experto"},
            {"email": "admin@example.com", "username": "admin", "rol": "admin"},
        ]

        for u in usuarios:
            if not User.objects.filter(email=u["email"]).exists() and not User.objects.filter(username=u["username"]).exists():
                User.objects.create_user(
                    email=u["email"],
                    username=u["username"],
                    password="test1234",
                    rol=u["rol"]
                )