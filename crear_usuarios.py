# crear_usuarios.py

from usuarios.models import Usuario

usuarios = [
    {"email": "normal@demo.com", "username": "normal", "rol": "normal"},
    {"email": "experto@demo.com", "username": "experto", "rol": "experto"},
    {"email": "admin@demo.com", "username": "admin", "rol": "admin"},
    {"email": "usuario@demo.com", "username": "usuario2", "rol": "normal"},
    {"email": "experto2@demo.com", "username": "experto2", "rol": "experto"},
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
