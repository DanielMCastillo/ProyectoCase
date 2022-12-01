from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Administradores(User):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=70)
    

class Alumnos(User):
    matricula = models.CharField(max_length=8, null=False, unique=True, primary_key=True)
    correo = models.CharField(max_length=70)
    nombre = models.TextField(max_length=50, null=False)
    nombre2 = models.TextField(max_length=50, null=True)
    apellidoP = models.TextField(max_length=50)
    apellidoM = models.TextField(max_length=50)
    telefono = models.CharField(max_length=10)
    
    def __str__(self):
        return self.matricula
    
