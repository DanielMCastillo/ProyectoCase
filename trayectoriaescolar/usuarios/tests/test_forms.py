from django.test import TestCase
from usuarios.forms import UserForm, ResponsableForm, AlumnoForm
from django.contrib.auth.models import User
from usuarios.models import Administradores, Responsables, Alumnos


class TestFormadmin(TestCase):

    def setUp(self, nombre='DanielCast', correo='amcdanymx@hotmail.com',
              password='Ronaldinho999.', repassword='Ronaldinho999.'):
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
            'commit': True

        }

    # Tests para cuenta de administrador

    def crear_usuario(self):
        User.objects.create_user(
            username='DanielMorales',
            password='Ronaldinho999.',
            email='danielmoralesc@gmail.com',
            repassword='Ronaldinho999.',
        )

    def test_admin_form_cuenta_guardada(self):
        form = UserForm(self.data)
        self.assertTrue(form.is_valid())

    def test_admin_form_cuenta_administrador(self):
        self.data['is_superuser'] = True
        form = UserForm(self.data)
        self.assertTrue(form.is_valid())

    def test_admin_form_password_espacios(self):
        self.data['repassword'] = ' '
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
            ['El usuario debe contener 8 o mas caracteres'])

    def test_admin_form_nombre_vacio_mensaje(self):
        self.data['username'] = ''
        form = UserForm(self.data)
        self.assertEqual(
            form.errors['username'],
            ['Este campo es obligatorio.'])

    def test_admin_form_email_invalido(self):
        self.data['email'] = 'a@hotmail'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_admin_form_email_vacio_mensaje(self):
        self.data['email'] = ''
        form = UserForm(self.data)
        self.assertEqual(form.errors['email'], [
            'Este campo es obligatorio.'])

    def test_admin_form_email_invalido_mensaje(self):
        self.data['email'] = 'jasg15_@hotmail'
        form = UserForm(self.data)
        self.assertEqual(form.errors['email'], [
            'Introduzca una direcci??n de correo electr??nico v??lida.'])

    def test_admin_form_password_invalido(self):
        self.data['password'] = 'ronaldinho999.'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_admin_form_password_invalido_mensaje(self):
        self.data['password'] = 'ay22'
        form = UserForm(self.data)
        self.assertEqual(form.errors['password'], [
            'La contrase??a debe contener al menos 8 caracteres'])

    def test_admin_form_password_re_requerido(self):
        self.data['repassword'] = ''
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_admin_form_password_re_con_espacios(self):
        self.data['repassword'] = 'Daniel Cas.'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_admin_form_password_formato_invalido(self):
        self.data['repassword'] = 'danielcast'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_admin_form_password_re_diferente_a_password(self):
        self.data['password'] = 'Ronaldinho999.'
        self.data['repassword'] = 'Ronaldinho'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_admin_form_password_re_mas_caracteres(self):
        self.data['repassword'] = 'amcdanymx'*8
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_admin_form_username_invalido_mensaje(self):
        self.data['username'] = 'hola amigo'
        form = UserForm(self.data)
        self.assertEqual(form.errors['username'], [
            'El nombre de usuario no debe contener espacios'])

    def test_admin_form_username_invalido2_mensaje(self):
        self.data['username'] = 'HOLA###$$$'
        form = UserForm(self.data)
        self.assertEqual(form.errors['username'], [
            'El nombre de usuario no debe contener caracteres especiales'])

    def test_admin_form_password_re_min_caracteres(self):
        self.data['repassword'] = 'aaa'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_admin_form_password_mayusculas(self):
        self.data['repassword'] = 'Ronaldinho999.'
        form = UserForm(self.data)
        self.assertTrue(form.is_valid())

    def test_admin_contrase??a_con_almenos_una_letra(self):
        self.data['password'] = '123456789'
        form = UserForm(self.data)
        self.assertEqual(form.errors['password'], [
            'La contrase??a debe contener al menos una letra'])

    def test_admin_contrase??a_con_mayuscula(self):
        self.data['password'] = 'holaaaaa.'
        form = UserForm(self.data)
        self.assertEqual(form.errors['password'], [
            'La contrase??a debe contener al menos una letra mayuscula'])

    def test_admin_contrase??a_con_letra_minuscula(self):
        self.data['password'] = 'HOLAAAAAA'
        form = UserForm(self.data)
        self.assertEqual(form.errors['password'], [
            'La contrase??a debe contener al menos una letra minuscula'])

    def test_admin_contrase??a_con_minuscula(self):
        self.data['password'] = 'Juanitooo22'
        form = UserForm(self.data)
        self.assertEqual(form.errors['password'], [
            'La contrase??a debe contener al menos un caracter especial'])

    def test_admin_contrase??a_con_numero(self):
        self.data['password'] = 'Juanitooo.'
        form = UserForm(self.data)
        self.assertEqual(form.errors['password'], [
            'La contrase??a debe contener al menos un n??mero'])

    def test_user_form_form_valid_data(self):
        form = UserForm(data={
            'username': 'DanielMorales',
            'email': 'danielmoralescast@gmail.com',
            'password': 'Ronaldinho999.',
            'repassword': 'Ronaldinho999.'
        })
        self.assertTrue(form.is_valid())


class TestFormResponsable(TestCase):

    def setUp(self, username='DanielCast', nombre='Daniel', nombre2='Alejandro',
              apellidoP='Morales', apellidoM='Castillo', email='amcdanymx@hotmail.com',
              programa_academico='IS', unidad_academica='IE',
              password='Ronaldinho999.', repassword='Ronaldinho999.'):
        self.responsable = Responsables(
            username=username,
            nombre=nombre,
            nombre2=nombre2,
            apellidoP=apellidoP,
            apellidoM=apellidoM,
            email=email,
            programa_academico=programa_academico,
            unidad_academica=unidad_academica,
            password=password,
            is_superuser=False,
            is_staff=True
        )

        self.data = {
            'username': username,
            'nombre': nombre,
            'nombre2': nombre2,
            'apellidoP': apellidoP,
            'apellidoM': apellidoM,
            'email': email,
            'unidad_academica': unidad_academica,
            'programa_academico': programa_academico,
            'password': password,
            'repassword': repassword,
            'is_superuser': False,
            'is_staff': True,
            'commit': True

        }
    # Pruebas de Responsable

    def crear_Responsable(self):
        Responsables.objects.create_user(
            username='DanielCast',
            nombre='Daniel',
            nombre2='Alejandro',
            apellidoP='Morales',
            apellidoM='Castillo',
            email='amcdanymx@hotmail.com',
            programa_academico='IS',
            unidad_academica='IE',
            password='Ronaldinho999.',
            repassword='Ronaldinho999.'
        )

    def test_responsable_form_cuenta_guardada(self):
        form = ResponsableForm(self.data)
        self.assertTrue(form.is_valid())

    def test_responsable_form_cuenta_responsable(self):
        self.data['is_staff'] = True
        form = ResponsableForm(self.data)
        self.assertTrue(form.is_valid())

    def test_responsable_form_password_espacios(self):
        self.data['repassword'] = ' '
        form = ResponsableForm(self.data)
        self.assertFalse(form.is_valid())

    def test_responsable_form_valido(self):
        form = ResponsableForm(self.data)
        self.assertTrue(form.is_valid())

    def test_responsable_form_nombre_vacio(self):
        self.data['username'] = ''
        form = ResponsableForm(self.data)
        self.assertFalse(form.is_valid())

    def test_responsable_form_nombre_invalido_mensaje(self):
        self.data['username'] = 'asd'
        form = ResponsableForm(self.data)
        self.assertEqual(
            form.errors['username'],
            ['El usuario debe contener 8 o mas caracteres'])

    def test_responsable_form_nombre_vacio_mensaje(self):
        self.data['username'] = ''
        form = ResponsableForm(self.data)
        self.assertEqual(
            form.errors['username'],
            ['Este campo es obligatorio.'])

    def test_responsable_form_email_invalido(self):
        self.data['email'] = 'a@hotmail'
        form = ResponsableForm(self.data)
        self.assertFalse(form.is_valid())

    def test_responsable_form_email_vacio_mensaje(self):
        self.data['email'] = ''
        form = ResponsableForm(self.data)
        self.assertEqual(form.errors['email'], [
            'Este campo es obligatorio.'])

    def test_responsable_form_email_invalido_mensaje(self):
        self.data['email'] = 'jasg15_@hotmail'
        form = ResponsableForm(self.data)
        self.assertEqual(form.errors['email'], [
            'Introduzca una direcci??n de correo electr??nico v??lida.'])

    def test_responsable_form_password_invalido(self):
        self.data['password'] = 'ronaldinho999.'
        form = ResponsableForm(self.data)
        self.assertFalse(form.is_valid())

    def test_responsable_form_password_invalido_mensaje(self):
        self.data['password'] = 'ay22'
        form = ResponsableForm(self.data)
        self.assertEqual(form.errors['password'], [
            'La contrase??a debe contener al menos 8 caracteres'])

    def test_responsable_form_password_re_requerido(self):
        self.data['repassword'] = ''
        form = ResponsableForm(self.data)
        self.assertFalse(form.is_valid())

    def test_responsable_form_password_re_con_espacios(self):
        self.data['repassword'] = 'Daniel Cas.'
        form = ResponsableForm(self.data)
        self.assertFalse(form.is_valid())

    def test_responsable_form_password_formato_invalido(self):
        self.data['repassword'] = 'danielcast'
        form = ResponsableForm(self.data)
        self.assertFalse(form.is_valid())

    def test_responsable_form_password_re_diferente_a_password(self):
        self.data['password'] = 'Ronaldinho999.'
        self.data['repassword'] = 'Ronaldinho'
        form = ResponsableForm(self.data)
        self.assertFalse(form.is_valid())

    def test_responsable_form_password_re_mas_caracteres(self):
        self.data['repassword'] = 'amcdanymx'*8
        form = ResponsableForm(self.data)
        self.assertFalse(form.is_valid())

    def test_responsable_form_username_invalido_mensaje(self):
        self.data['username'] = 'hola amigo'
        form = ResponsableForm(self.data)
        self.assertEqual(form.errors['username'], [
            'El nombre de usuario no debe contener espacios'])

    def test_responsable_form_username_invalido2_mensaje(self):
        self.data['username'] = 'HOLA###$$$'
        form = ResponsableForm(self.data)
        self.assertEqual(form.errors['username'], [
            'El nombre de usuario no debe contener caracteres especiales'])

    def test_responsable_form_password_re_min_caracteres(self):
        self.data['repassword'] = 'aaa'
        form = ResponsableForm(self.data)
        self.assertFalse(form.is_valid())

    def test_responsable_form_password_mayusculas(self):
        self.data['repassword'] = 'Ronaldinho999.'
        form = ResponsableForm(self.data)
        self.assertTrue(form.is_valid())

    def test_responsable_contrase??a_con_almenos_una_letra(self):
        self.data['password'] = '123456789'
        form = ResponsableForm(self.data)
        self.assertEqual(form.errors['password'], [
                         'La contrase??a debe contener al menos una letra'])

    def test_responsable_contrase??a_con_mayuscula(self):
        self.data['password'] = 'holaaaaa.'
        form = ResponsableForm(self.data)
        self.assertEqual(form.errors['password'], [
                         'La contrase??a debe contener al menos una letra mayuscula'])

    def test_responsable_contrase??a_con_letra_minuscula(self):
        self.data['password'] = 'HOLAAAAAA'
        form = ResponsableForm(self.data)
        self.assertEqual(form.errors['password'], [
                         'La contrase??a debe contener al menos una letra minuscula'])

    def test_responsable_contrase??a_con_minuscula(self):
        self.data['password'] = 'Juanitooo22'
        form = ResponsableForm(self.data)
        self.assertEqual(form.errors['password'], [
                         'La contrase??a debe contener al menos un caracter especial'])

    def test_responsable_contrase??a_con_numero(self):
        self.data['password'] = 'Juanitooo.'
        form = ResponsableForm(self.data)
        self.assertEqual(form.errors['password'], [
                         'La contrase??a debe contener al menos un n??mero'])

    def test_apellido_requerido(self):
        self.data['apellidoP'] = ''
        form = ResponsableForm(self.data)
        self.assertEqual(form.errors['apellidoP'], [
                         'Este campo es obligatorio.'])

    def test_apellido_no_requerido(self):
        self.data['apellidoM'] = ''
        form = ResponsableForm(self.data)
        self.assertTrue(form.is_valid())

    def test_unidad_academica_requerido(self):
        self.data['unidad_academica'] = ''
        form = ResponsableForm(self.data)
        self.assertEqual(form.errors['unidad_academica'], [
                         'Este campo es obligatorio.'])

    def test_programa_academico_requerido(self):
        self.data['programa_academico'] = ''
        form = ResponsableForm(self.data)
        self.assertEqual(form.errors['programa_academico'], [
                         'Este campo es obligatorio.'])

    def user_form_form_valid_data(self):
        form = ResponsableForm(data={
            'username': 'DanielCast',
            'nombre': 'Daniel',
            'nombre2': 'Alejandro',
            'apellidoP': 'Morales',
            'apellidoM': 'Castillo',
            'email': 'amcdanymx@hotmail.com',
            'programa_academico': 'IS',
            'unidad_academica': 'IE',
            'password': 'Ronaldinho999.',
            'repassword': 'Ronaldinho999.'
        })
        self.assertTrue(form.is_valid())


# Test alumnos
class TestFormAlumnos(TestCase):

    def setUp(self, username='12345678', nombre='Daniel', nombre2='Alejandro', apellidoP='Morales',
              apellidoM='Castillo', email='amcdanymx@hotmail.com', telefono='1234567890',
              password='Ronaldinho999.', repassword='Ronaldinho999.'):
        self.alumno = Alumnos(
            username=username,
            nombre=nombre,
            nombre2=nombre2,
            apellidoP=apellidoP,
            apellidoM=apellidoM,
            email=email,
            telefono=telefono,
            password=password,
            is_superuser=False,
            is_staff=False
        )

        self.data = {
            'username': username,
            'nombre': nombre,
            'nombre2': nombre2,
            'apellidoP': apellidoP,
            'apellidoM': apellidoM,
            'email': email,
            'telefono': telefono,
            'password': password,
            'repassword': repassword,
            'is_superuser': False,
            'is_staff': True,
            'commit': True

        }
    # Pruebas de alumno

    def crear_alumno(self):
        Alumnos.objects.create_user(
            username='12345678',
            nombre='Daniel',
            nombre2='Alejandro',
            apellidoP='Morales',
            apellidoM='Castillo',
            email='amcdanymx@hotmail.com',
            programa_academico='IS',
            unidad_academica='IE',
            password='Ronaldinho999.',
            repassword='Ronaldinho999.'
        )

    def test_alumno_form_cuenta_guardada(self):
        form = AlumnoForm(self.data)
        self.assertTrue(form.is_valid())

    def test_alumno_form_cuenta_alumno(self):
        self.data['is_staff'] = False
        form = AlumnoForm(self.data)
        self.assertTrue(form.is_valid())

    def test_alumno_form_password_espacios(self):
        self.data['repassword'] = ' '
        form = AlumnoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_alumno_form_matricula_chica(self):
        self.data['username'] = '12345'
        form = AlumnoForm(self.data)
        self.assertTrue(form.errors['username'],
                        ['La matr??cula debe contener exactamente 8 d??gitos'])

    def test_alumno_form_matricula_letras(self):
        self.data['username'] = '12345abc'
        form = AlumnoForm(self.data)
        self.assertTrue(form.errors['username'],
                        ['La matr??cula debe contener solo n??meros'])

    def test_alumno_form_password_invalido(self):
        self.data['password'] = 'ronaldinho999.'
        form = AlumnoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_alumno_form_password_invalido_mensaje(self):
        self.data['password'] = 'ay22'
        form = AlumnoForm(self.data)
        self.assertEqual(form.errors['password'], [
            'La contrase??a debe contener al menos 8 caracteres'])

    def test_alumno_form_password_re_requerido(self):
        self.data['repassword'] = ''
        form = AlumnoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_alumno_form_password_re_con_espacios(self):
        self.data['repassword'] = 'Daniel Cas.'
        form = AlumnoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_alumno_form_password_formato_invalido(self):
        self.data['repassword'] = 'danielcast'
        form = AlumnoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_alumno_form_password_re_diferente_a_password(self):
        self.data['password'] = 'Ronaldinho999.'
        self.data['repassword'] = 'Ronaldinho'
        form = AlumnoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_alumno_form_password_re_mas_caracteres(self):
        self.data['repassword'] = 'amcdanymx'*8
        form = AlumnoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_alumno_form_username_invalido_mensaje(self):
        self.data['username'] = 'hola amigo'
        form = AlumnoForm(self.data)
        self.assertEqual(form.errors['username'], [
            'La matr??cula debe contener exactamente 8 d??gitos'])

    def test_alumno_form_username_invalido2_mensaje(self):
        self.data['username'] = 'HOLA###$$$'
        form = AlumnoForm(self.data)
        self.assertEqual(form.errors['username'], [
            'La matr??cula debe contener exactamente 8 d??gitos'])

    def test_alumno_form_password_re_min_caracteres(self):
        self.data['repassword'] = 'aaa'
        form = AlumnoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_alumno_form_password_mayusculas(self):
        self.data['repassword'] = 'Ronaldinho999.'
        form = AlumnoForm(self.data)
        self.assertTrue(form.is_valid())

    def test_alumno_contrase??a_con_almenos_una_letra(self):
        self.data['password'] = '123456789'
        form = AlumnoForm(self.data)
        self.assertEqual(form.errors['password'], [
                         'La contrase??a debe contener al menos una letra'])

    def test_alumno_contrase??a_con_mayuscula(self):
        self.data['password'] = 'holaaaaa.'
        form = AlumnoForm(self.data)
        self.assertEqual(form.errors['password'], [
                         'La contrase??a debe contener al menos una letra mayuscula'])

    def test_alumno_contrase??a_con_letra_minuscula(self):
        self.data['password'] = 'HOLAAAAAA'
        form = AlumnoForm(self.data)
        self.assertEqual(form.errors['password'], [
                         'La contrase??a debe contener al menos una letra minuscula'])

    def test_alumno_contrase??a_con_minuscula(self):
        self.data['password'] = 'Juanitooo22'
        form = AlumnoForm(self.data)
        self.assertEqual(form.errors['password'], [
                         'La contrase??a debe contener al menos un caracter especial'])

    def test_alumno_contrase??a_con_numero(self):
        self.data['password'] = 'Juanitooo.'
        form = AlumnoForm(self.data)
        self.assertEqual(form.errors['password'], [
                         'La contrase??a debe contener al menos un n??mero'])

    def test_alumno_telefono_no_numero(self):
        self.data['telefono'] = 'Juanitooo.'
        form = AlumnoForm(self.data)
        self.assertEqual(form.errors['telefono'], [
                         'El telefono debe ser un n??mero'])

    def test_alumno_telefono_chico(self):
        self.data['telefono'] = '123456'
        form = AlumnoForm(self.data)
        self.assertEqual(form.errors['telefono'], [
                         'El telefono debe ser un n??mero de 10 d??gitos'])

    def alumno_form_form_valid_data(self):
        form = AlumnoForm(data={
            'username': '12345678',
            'nombre': 'Daniel',
            'nombre2': 'Alejandro',
            'apellidoP': 'Morales',
            'apellidoM': 'Castillo',
            'email': 'amcdanymx@hotmail.com',
            'telefono': '1234567890',
            'password': 'Ronaldinho999.',
            'repassword': 'Ronaldinho999.'
        })
        self.assertTrue(form.is_valid())
