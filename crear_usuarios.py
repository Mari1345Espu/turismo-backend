# crear_usuarios.py

from usuarios.models import Usuario

usuarios = [
    {"email": "normal@demo.com", "username": "normal", "rol": "normal"},
    {"email": "experto@demo.com", "username": "experto", "rol": "experto"},
    {"email": "admin@demo.com", "username": "admin", "rol": "admin"},
]

for u in usuarios:
    if not Usuario.objects.filter(email=u["email"]).exists():
        Usuario.objects.create_user(
            email=u["email"],
            username=u["username"],
            password="test1234",
            rol=u["rol"]
        )
        print(f"✅ Usuario {u['email']} creado.")
    else:
        print(f"ℹ️ Usuario {u['email']} ya existe.")
