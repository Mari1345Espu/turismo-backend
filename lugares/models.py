from django.db import models
from django.conf import settings
# Create your models here.


class LugarTuristico(models.Model):
    CATEGORIAS = [
        ('restaurante', 'Restaurante'),
        ('atraccion', 'Atracción'),
        ('hospedaje', 'Hospedaje'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    direccion = models.CharField(max_length=200)
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    imagen_principal = models.ImageField(upload_to='lugares/', null=True, blank=True)
    calificacion_promedio = models.FloatField(default=0)

    def __str__(self):
        return self.nombre

class ComentarioLugar(models.Model):
    lugar = models.ForeignKey(LugarTuristico, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField()
    calificacion = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.lugar.nombre} ({self.calificacion})"

class RutaSugerida(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    lugares = models.ManyToManyField(LugarTuristico, related_name='rutas')

    def __str__(self):
        return self.nombre

class Favorito(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favoritos')
    lugar = models.ForeignKey(LugarTuristico, on_delete=models.CASCADE, related_name='favorito_de')
    fecha_guardado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'lugar')  # Evita duplicados

    def __str__(self):
        return f"{self.usuario.username} ❤️ {self.lugar.nombre}"
