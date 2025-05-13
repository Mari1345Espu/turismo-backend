from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Register your models here.
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['email', 'username', 'rol', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('rol',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('rol',)}),
    )

admin.site.register(Usuario, UsuarioAdmin)