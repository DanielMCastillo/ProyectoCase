from django.test import TestCase
from usuarios.models import Administradores


class TestSmoke(TestCase):


    def AdministradoresTest(self):
        self.admin = Administradores.objects.create(
            username='DanielCastillo',
            email = 'amcdanymx3@gmail.com',
            password = 'Ronaldinho999.',
            repassword='Ronaldinho999.'
        )
        