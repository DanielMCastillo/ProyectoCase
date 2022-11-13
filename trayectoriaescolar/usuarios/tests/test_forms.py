from django.test import TestCase
from usuarios.forms import UserForm
from django.contrib.auth.models import User
from usuarios.models import Administradores

class TestFormUsuario(TestCase):

    def setUp(self, nombre='DanielCast', correo='amcdanymx@hotmail.com',password='Ronaldinho999.', repassword='Ronaldinho999.'):
        self.usuario = Administradores(
            username=nombre,
            email=correo,
            password=password,
            is_superuser=True
        )
    
        self.data = {
            'username': nombre,
            'email': correo,
            'password': password,
            'repassword': repassword,
            'is_superuser': True
        }

    # Tests para cuenta de administrador
    def test_usuario_form_cuenta_administrador(self):
        self.data['is_superuser'] = True
        form = UserForm(self.data)
        self.assertTrue(form.is_valid())
    
    def test_usuario_form_password_re_espacios(self):
        self.data['password_re'] = ' '
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())
    
    def test_usuario_form_valido(self):
        form = UserForm(self.data)
        self.assertTrue(form.is_valid())

    def test_usuario_form_nombre_vacio(self):
        self.data['username'] = ''
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_nombre_invalido_mensaje(self):
        self.data['username'] = 'asd'
        form = UserForm(self.data)
        self.assertEqual(
            form.errors['username'],
            ['El nombre de usuario no sigue el formato'
            + ' solicitado, favor de verificarlo.'])

    def test_usuario_form_nombre_vacio_mensaje(self):
        self.data['username'] = ''
        form = UserForm(self.data)
        self.assertEqual(
            form.errors['username'],
            ['El nombre de usuario es requerido, favor de completarlo.'])

    def test_usuario_form_email_invalido(self):
        self.data['email'] = 'a@hotmail'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_email_vacio_mensaje(self):
        self.data['email'] = ''
        form = UserForm(self.data)
        self.assertEqual(form.errors['email'], [
                        'El correo es requerido, favor de completarlo.'])

    def test_usuario_form_email_invalido_mensaje(self):
        self.data['email'] = 'jasg15_@hotmail'
        form = UserForm(self.data)
        self.assertEqual(form.errors['email'], [
                        'Favor de ingresar un formato de correo válido.'])

    def test_usuario_form_password_invalido(self):
        self.data['password'] = 'Ronaldinho999.'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_invalido_mensaje(self):
        self.data['password'] = 'ay22'
        form = UserForm(self.data)
        self.assertEqual(form.errors['password'], ['La contraseña no es correcta'])

    def test_usuario_form_password_re_requerido(self):
        self.data['password_re'] = ''
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_re_con_espacios(self):
        self.data['password_re'] = 'Daniel Cas. '
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_re_formato_invalido(self):
        self.data['password_re'] = 'danielcast'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_re_diferente_a_password(self):
        self.data['password'] = 'Ronaldinho999.'
        self.data['password_re'] = 'Ronaldinho'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_re_mas_caracteres(self):
        self.data['password_re'] = 'amcdanymx'*8
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_re_min_caracteres(self):
        self.data['password_re'] = 'aaa'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())