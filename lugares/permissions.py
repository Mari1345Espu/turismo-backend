from rest_framework import permissions

class EsExpertoOAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol in ['experto', 'admin']

class EsDueñoOAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.usuario == request.user or request.user.rol == 'admin'