from django.test import TestCase
from usuarios.models import Administradores
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class TestModels(TestCase):

    def setUp(self, nombre='Juanito20',
            correo='juanito20@gmail.com', password='Juanito20.'):
        self.usuario = Administradores(
            username=nombre,
            email=correo,
            password=password,
            is_superuser=True
        )

    def test_return_object_admin(self):
        self.usuario.save()
        self.assertEqual(User.objects.first().username, self.usuario.nombre)

    def test_nombre_es_requerido(self):
        usuario = User(
            email='juanito20@hotmail.com',
            password='Juan20.'
        )
        with self.assertRaises(ValidationError):
            usuario.full_clean()

    def test_nombre_usuario_min_8_char(self):
        self.usuario.username = 'juan20'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_nombre_usuario_no_acepta_espacios(self):
        self.usuario.username = 'juan 20'
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()

    def test_correo_es_requerido(self):
        usuario = User(
            username='juan20',
            password='juanito20@'
        )
        self.administrativo.usuario = usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_email_incorrecto(self):
        self.usuario.email = 'juanito@gmail'
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()

    def test_email_incorrecto_espacios(self):
        self.usuario.email = 'juanito20@gmail. com'
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()

    def test_password_es_requerido(self):
        usuario = User(
            username='Juan20',
            email='juanito20@hotmail.com'
        )
        with self.assertRaises(ValidationError):
            usuario.full_clean()

    def test_password_incorrecto(self):
        self.usuario.password = 'juanito'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_password_correcto(self):
        self.usuario.password = 'Juanito20.'
        self.usuario.full_clean()
        self.usuario.save()
        self.assertEqual(User.objects.first().password, self.usuario.password)

    def test_password_incorrecto_min_caracteres(self):
        self.usuario.password = 'jor'
        try:
            self.usuario.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['password'][0])
            self.assertEqual(
                msg,
                'La contraseña no sigue el formato solicitado: Mínimo 8 '
                + 'caracteres, máximo 50 caracteres mínimo una mayúscula,'
                + ' mínimo una minúscula, mínimo un número y mínimo un '
                + 'símbolo, favor de verificarla.')
