from django.db import models
from django.contrib.auth.models import AbstractUser
from lugares.models import LugarTuristico

# Create your models here.
class Usuario(AbstractUser):
    ROL_CHOICES = (
        ('normal', 'Usuario normal'),
        ('experto', 'Usuario experto'),
        ('admin', 'Administrador'),
    )
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default='normal')
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Email como USERNAME_FIELD

    def __str__(self):
        return f'{self.email} ({self.rol})'
    
    