from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Administradores(User):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=70)
    
    
