# crear_usuarios.py

from usuarios.models import Usuario

usuarios = [
    {"email": "usuario3@demo.com", "username": "normal", "rol": "normal"},
    {"email": "experto3@demo.com", "username": "experto", "rol": "experto"},
    {"email": "admin2@demo.com", "username": "admin", "rol": "admin"},
    {"email": "usuario4@demo.com", "username": "usuario4", "rol": "normal"},
    {"email": "experto4@demo.com", "username": "experto4s", "rol": "experto"},
]

for u in usuarios:
    if not Usuario.objects.filter(email=u["email"]).exists():
        Usuario.objects.create_user(
            email=u["email"],
            username=u["username"],
            password="test1234",
            rol=u["rol"]
        )
        print(f" Usuario {u['email']} creado.")
    else:
        print(f"ℹ Usuario {u['email']} ya existe.")