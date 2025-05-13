# 🌍 Turismo App - Backend

Aplicación web y móvil para la gestión de lugares turísticos, rutas sugeridas y comunidad. Desarrollada con Django REST Framework. Incluye autenticación por roles y pruebas automatizadas con TDD.

##  Tecnologías utilizadas

- Python 3.11
- Django 5.x
- Django REST Framework
- Djoser + JWT
- SQLite (modo desarrollo)
- Behave (opcional, para pruebas BDD)
- Postman (para pruebas manuales)

---

##  Roles de usuario

| Rol        | Permisos principales                                                |
|------------|---------------------------------------------------------------------|
| **Normal** | Ver lugares, comentar, agregar favoritos                            |
| **Experto**| Crear y editar lugares, rutas sugeridas                             |
| **Admin**  | Acceso completo al sistema                                          |

---

##  Funcionalidades

- Autenticación JWT con Djoser
- Registro, login, edición de perfil, cambio y recuperación de contraseña
- Gestión de lugares turísticos (por expertos o admins)
- Sistema de favoritos por usuario
- Comentarios y calificaciones por lugar
- Rutas sugeridas por expertos
- Filtros por categoría, calificación y ordenamiento por cercanía
- Restricciones de acceso según rol

---

## Pruebas

###  TDD con `APITestCase
Ejecuatrlas en la terminal con los comandos: 
'python manage.py test usuarios'
'python manage.py test lugares'
