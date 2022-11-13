from django.test import TestCase
from usuarios.models import Administradores
from django.core.exceptions import ValidationError


class TestSmoke(TestCase):


    def AdministradoresTest(self):
        self.admin = Administradores.objects.create(
            nombre='DanielCastillo',
            correo = 'amcdanymx3@gmail.com',
            contraseña = 'Ronaldinho999.',
            confirmar='Ronaldinho999.'
        )
        