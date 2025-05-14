import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'turismo_project.settings')

# --- Bloque temporal para migrar y crear superusuario ---
import django
django.setup()

from django.core.management import call_command
from django.contrib.auth import get_user_model

# Ejecutar migraciones
call_command('migrate', interactive=False)

# Crear superusuario si no existe
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin1234'
    )
# ---------------------------------------------------------

application = get_wsgi_application()




