from behave import given, when, then
from rest_framework.test import APIClient
from usuarios.models import Usuario
from lugares.models import LugarTuristico

@given('un usuario con rol "{rol}" y clave "{clave}"')
def step_impl(context, rol, clave):
    email = f"{rol}@example.com"
    Usuario.objects.create_user(
        email=email,
        username=rol,
        password=clave,
        rol=rol
    )
    context.email = email
    context.password = clave

@given('estoy autenticado como "{email}"')
def step_impl(context, email):
    user = Usuario.objects.get(email=email)
    context.client = APIClient()
    context.client.force_authenticate(user=user)

@when('intento crear un lugar con nombre "{nombre}"')
def step_impl(context, nombre):
    data = {
        "nombre": nombre,
        "descripcion": "Descripción de prueba",
        "categoria": "atraccion",
        "direccion": "Calle Falsa 123",
        "latitud": 4.5,
        "longitud": -74.1
    }
    context.response = context.client.post("/api/lugares/", data, format='json')

@then('la respuesta debe ser {codigo}')
def step_impl(context, codigo):
    assert context.response.status_code == int(codigo), f"Esperado {codigo}, recibido {context.response.status_code}. Respuesta: {context.response.data}"
