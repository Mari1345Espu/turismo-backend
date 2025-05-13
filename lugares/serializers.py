from rest_framework import serializers
from .models import LugarTuristico, ComentarioLugar, RutaSugerida, Favorito

class LugarTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LugarTuristico
        fields = '__all__'

class ComentarioLugarSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ComentarioLugar
        fields = '__all__'
        read_only_fields = ['usuario', 'fecha']

class RutaSugeridaSerializer(serializers.ModelSerializer):
    lugares = LugarTuristicoSerializer(many=True, read_only=True)
    lugar_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=LugarTuristico.objects.all(), write_only=True, source='lugares'
    )

    class Meta:
        model = RutaSugerida
        fields = ['id', 'nombre', 'descripcion', 'lugares', 'lugar_ids']

class FavoritoSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField(read_only=True)
    lugar_detalle = LugarTuristicoSerializer(source='lugar', read_only=True)

    class Meta:
        model = Favorito
        fields = ['id', 'usuario', 'lugar', 'lugar_detalle', 'fecha_guardado']
        read_only_fields = ['usuario', 'fecha_guardado']