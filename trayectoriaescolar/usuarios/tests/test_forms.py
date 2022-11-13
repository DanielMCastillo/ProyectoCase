from django.test import TestCase
from usuarios.forms import UserForm
from django.contrib.auth.models import User
from usuarios.models import Administradores

class TestFormadmin(TestCase):

    def setUp(self, nombre='DanielCast', correo='amcdanymx@hotmail.com',password='Ronaldinho999.', repassword='Ronaldinho999.'):
        self.admin = Administradores(
            username=nombre,
            email=correo,
            password=password,
            is_superuser=True,
        )
        
    
        self.data = {
            'username': nombre,
            'email': correo,
            'password': password,
            'repassword': repassword,
            'is_superuser': True,
            'commit' : True
            
        }
        

    # Tests para cuenta de administrador
    
    def crear_usuario(self):
        User.objects.create_user(
            username='DanielMorales',
            password='Ronaldinho999.',
            email='danielmoralesc@gmail.com',
            repassword='Ronaldinho999.',
        )
    
    def test_admin_form_cuenta_administrador(self):
        self.data['is_superuser'] = True
        form = UserForm(self.data)
        self.assertTrue(form.is_valid())
    
    def test_admin_form_cuenta_guardada(self):
        form = UserForm(self.data)
        self.assertTrue(form.is_valid())
        
    def test_admin_form_cuenta_administrador(self):
        self.data['is_superuser'] = True
        form = UserForm(self.data)
        self.assertTrue(form.is_valid())
    
    def test_admin_form_password_espacios(self):
        self.data['password_re'] = ' '
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())
    
    def test_admin_form_valido(self):
        form = UserForm(self.data)
        self.assertTrue(form.is_valid())

    def test_admin_form_nombre_vacio(self):
        self.data['username'] = ''
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_admin_form_nombre_invalido_mensaje(self):
        self.data['username'] = 'asd'
        form = UserForm(self.data)
        self.assertEqual(
            form.errors['username'],
            ['El nombre de admin no sigue el formato'
            + ' solicitado, favor de verificarlo.'])

    def test_admin_form_nombre_vacio_mensaje(self):
        self.data['username'] = ''
        form = UserForm(self.data)
        self.assertEqual(
            form.errors['username'],
            ['El nombre de admin es requerido, favor de completarlo.'])

    def test_admin_form_email_invalido(self):
        self.data['email'] = 'a@hotmail'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_admin_form_email_vacio_mensaje(self):
        self.data['email'] = ''
        form = UserForm(self.data)
        self.assertEqual(form.errors['email'], [
                        'El correo es requerido, favor de completarlo.'])

    def test_admin_form_email_invalido_mensaje(self):
        self.data['email'] = 'jasg15_@hotmail'
        form = UserForm(self.data)
        self.assertEqual(form.errors['email'], [
                        'Favor de ingresar un formato de correo válido.'])

    def test_admin_form_password_invalido(self):
        self.data['password'] = 'Ronaldinho999.'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())
    
    def test_admin_form_password_invalido(self):
        self.data['password'] = 'HOLAAAAA.'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_admin_form_password_invalido_mensaje(self):
        self.data['password'] = 'ay22'
        form = UserForm(self.data)
        self.assertEqual(form.errors['password'], ['La contraseña no es correcta'])

    def test_admin_form_password_re_requerido(self):
        self.data['password_re'] = ''
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_admin_form_password_re_con_espacios(self):
        self.data['password_re'] = 'Daniel Cas. '
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_admin_form_password_formato_invalido(self):
        self.data['password_re'] = 'danielcast'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())
    

    def test_admin_form_password_re_diferente_a_password(self):
        self.data['password'] = 'Ronaldinho999.'
        self.data['password_re'] = 'Ronaldinho'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_admin_form_password_re_mas_caracteres(self):
        self.data['password_re'] = 'amcdanymx'*8
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())
        
    def test_admin_form_username_invalido_mensaje(self):
        self.data['username'] = 'hola amigo'
        form = UserForm(self.data)
        self.assertEqual(form.errors['username'], [
                        'El nombre de usuario no puede contener espacios.'])
    
    def test_admin_form_username_invalido2_mensaje(self):
        self.data['username'] = 'HOLA###$$$'
        form = UserForm(self.data)
        self.assertEqual(form.errors['username'], [
                        'El nombre de usuario no puede contener caracteres especiales.'])

    def test_admin_form_password_re_min_caracteres(self):
        self.data['password_re'] = 'aaa'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())
    
    def test_admin_form_password_mayusculas(self):
        self.data['password_re'] = 'Ronaldinho999.'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())
        
    def test_admin_contraseña_con_almenos_una_letra(self):
        self.data['password'] = '123456789'
        form = UserForm(self.data)
        self.assertEqual(form.errors['password'], ['La contraseña debe contener al menos una letra.'])
    
    def test_admin_contraseña_con_mayuscula(self):
        self.data['password'] = 'holaaaaa.'
        form = UserForm(self.data)
        self.assertEqual(form.errors['password'], ['La contraseña debe contener al menos una letra mayuscula.'])
    
    def test_admin_contraseña_con_letra_minuscula(self):
        self.data['password'] = 'HOLAAAAAA'
        form = UserForm(self.data)
        self.assertEqual(form.errors['password'], ['La contraseña debe contener al menos una minuscula.'])
    
    def test_admin_contraseña_con_minuscula(self):
        self.data['password'] = 'Juanitooo22'
        form = UserForm(self.data)
        self.assertEqual(form.errors['password'], ['El nombre de usuario debe contener al menos un caracter especial.'])    

    def test_admin_contraseña_con_numero(self):
        self.data['password'] = 'Juanitooo.'
        form = UserForm(self.data)
        self.assertEqual(form.errors['password'], ['El nombre de usuario debe contener al menos un numero.']) 
    
    def test_admin_form_password_diferente_a_confirmar(self):
        self.data['password'] = 'Ronaldinho999.'
        self.data['password_re'] = 'pedroooo'
        form = UserForm(self.data)
        self.assertEqual(form.errors['password'], ['Las contraseñas son diferentes']) 
        
    
    def user_form_form_valid_data(self):
        form = UserForm(data={
            'username': 'DanielMorales',
            'email': 'danielmoralescast@gmail.com',
            'password': 'Ronaldinho999.',
            'repassword': 'Ronaldinho999.'
        })
        self.assertTrue(form.is_valid())
    