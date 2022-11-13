from django.test import TestCase
from usuarios.models import Administradores
from django.core.exceptions import ValidationError


class TestSmoke(TestCase):


    def AdministradoresTest(self):
        self.admin = Administradores.objects.create(
            nombre='Categoría 1',
            descripcion='Rollo de categoría'
        )
        self.admin = Administradores.objects.create(
            nombre='Consola',
            decripcion='Rollo',
            stock=5,
            genero='1',
            categoria=self.categoria
        )

    def test_insertar_admin_nuevo(self):
        self.assertEquals(Administradores.objects.count(),1)

    def test_verifica_longitud_nombre(self):
        self.categoria.nombre = 'k'*100
        with self.assertRaises(ValidationError):
            self.categoria.full_clean()
            
    def test_verifica_longitu_correo(self):
        self.admin.correo = 'k'*32
        
        with self.assertRaises(ValidationError):
            self.admin.full_clean()
