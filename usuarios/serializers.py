from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from .models import Usuario

class UsuarioCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = Usuario
        fields = ('id', 'email', 'username', 'password', 'rol')

class UsuarioSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = Usuario
        fields = ('id', 'email', 'username', 'rol')

class UsuarioSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = Usuario
        fields = ('id', 'email', 'username', 'rol')

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if not user.rol == 'admin':
            validated_data.pop('rol', None)  # Solo admin puede cambiar el rol
        return super().update(instance, validated_data)