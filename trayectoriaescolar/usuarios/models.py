from django.db import models
from django.contrib.auth.models import User

class Administradores(User):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=70)
    
class Responsables(User):
    correo = models.CharField(max_length=70)
    nombre = models.TextField(max_length=50, null=False)
    nombre2 = models.TextField(max_length=50, null=True, blank=True)
    apellidoP = models.TextField(max_length=50)
    apellidoM = models.TextField(max_length=50, null=True, blank=True)
    programa_academico = models.TextField(max_length=70, null=False)
    unidad_academica = models.TextField(max_length=50, null=False)

class Alumnos(User):
    correo = models.CharField(max_length=70)
    nombre = models.TextField(max_length=50, null=False)
    nombre2 = models.TextField(max_length=50, null=True, blank=True)
    apellidoP = models.TextField(max_length=50)
    apellidoM = models.TextField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):
        return self.matricula
    
