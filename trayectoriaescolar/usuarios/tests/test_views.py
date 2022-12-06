from django.test import TestCase
from django.contrib.auth.models import User
from usuarios.models import Responsables, Alumnos


class TestViewsCase(TestCase):
    def setUp(self):
        self.admin = User.objects.create(
            username='DanielAle',
            password='Ronaldinho999.',
            is_superuser=True,
            is_active=True,
            is_staff=True
        )
        self.admin.set_password('Ronaldinho999.')
        self.admin.save()
        self.client.login(username='DanielAle', password='Ronaldinho999.')

        self.responsable = Responsables.objects.create(
            username='DanielCast',
            nombre='Daniel',
            nombre2='Alejandro',
            apellidoP='Morales',
            apellidoM='Castillo',
            email='amcdanymx@hotmail.com',
            programa_academico='IS',
            unidad_academica='IE',
            password='Ronaldinho999.',
            is_superuser=False,
            is_staff=True,
            is_active=True
        )
        self.responsable.set_password('Ronaldinho999.')
        self.responsable.save()

        self.alumno = Alumnos.objects.create(
            username='12345678',
            nombre='Daniel',
            nombre2='Alejandro',
            apellidoP='Morales',
            apellidoM='Castillo',
            email='amcdanymx@hotmail.com',
            telefono='',
            password='Ronaldinho999.',
            is_superuser=False,
            is_staff=False,
            is_active=True
        )
        self.alumno.set_password('Ronaldinho999.')
        self.alumno.save()
        # self.test_guarda_Alumno()

    def test_login_staff_estatus(self):
        respuesta = self.client.get('/login/', {}, follow=True)
        self.assertEquals(respuesta.status_code, 200)

    def test_template_login_staff(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'login.html')

    def test_login_alumno_status(self):
        respuesta = self.client.get('', {}, follow=True)
        self.assertEquals(respuesta.status_code, 200)

    def test_template_login_alumno(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'login_alumno.html')

    def test_registrar_admin_estatus(self):
        self.deslogearse()
        self.logearseAdmin()
        respuesta = self.client.get(
            '/registro_de_administrador', {}, follow=True)
        self.assertEquals(respuesta.status_code, 200)

    def test_registrar_responsable_estatus(self):
        self.deslogearse()
        self.logearseAdmin()
        respuesta = self.client.get('/registro_responsable', {}, follow=True)
        self.assertEquals(respuesta.status_code, 200)

    def test_registrar_alumno_estatus(self):
        self.deslogearse()
        self.logearseAdmin()
        respuesta = self.client.get('/registro_alumno', {}, follow=True)
        self.assertEquals(respuesta.status_code, 200)

    def test_template_registro_admin(self):
        self.deslogearse()
        self.logearseAdmin()
        response = self.client.get('/registro_de_administrador')
        self.assertTemplateUsed(response, 'registro_de_administrador.html')

    def test_template_registro_responsable(self):
        self.deslogearse()
        self.logearseAdmin()
        response = self.client.get('/registro_responsable')
        self.assertTemplateUsed(response, 'registro_responsable.html')

    def test_template_registro_alumno(self):
        self.deslogearse()
        self.logearseAdmin()
        response = self.client.get('/registro_alumno')
        self.assertTemplateUsed(response, 'registro_alumno.html')

    def test_lista_adminisitradores_estatus(self):
        self.deslogearse()
        self.logearseAdmin()
        respuesta = self.client.get('/administradores', {}, follow=True)
        self.assertEquals(respuesta.status_code, 200)

    def test_lista_responsables_estatus(self):
        self.deslogearse()
        self.logearseAdmin()
        respuesta = self.client.get('/responsables', {}, follow=True)
        self.assertEquals(respuesta.status_code, 200)

    def test_lista_alumnos_estatus(self):
        self.deslogearse()
        self.logearseAdmin()
        respuesta = self.client.get('/alumnos', {}, follow=True)
        self.assertEquals(respuesta.status_code, 200)

    def test_template_lista_adminisitradores(self):
        self.deslogearse()
        self.logearseAdmin()
        response = self.client.get('/administradores', {}, follow=True)
        self.assertTemplateUsed(response, 'administradores.html')

    def test_template_lista_responsables(self):
        self.deslogearse()
        self.logearseAdmin()
        response = self.client.get('/responsables', {}, follow=True)
        self.assertTemplateUsed(response, 'responsables.html')

    def test_template_lista_alumnos(self):
        self.deslogearse()
        self.logearseAdmin()
        response = self.client.get('/alumnos', {}, follow=True)
        self.assertTemplateUsed(response, 'alumnos.html')

    def test_home_staff_status(self):
        self.deslogearse()
        self.logearseAdmin()
        respuesta = self.client.get('/home', {}, follow=True)
        self.assertEquals(respuesta.status_code, 200)

    def test_home_alumno_status(self):
        self.deslogearse()
        self.logearseAlumno()
        respuesta = self.client.get('/home_alumno', {}, follow=True)
        self.assertEquals(respuesta.status_code, 200)

    def test_template_home_staff(self):
        self.deslogearse()
        self.logearseAdmin()
        response = self.client.get('/home', {}, follow=True)
        self.assertTemplateUsed(response, 'home_case.html')

    def test_template_home_alumno(self):
        self.deslogearse()
        self.logearseAlumno()
        response = self.client.get('/home_alumno', {}, follow=True)
        self.assertTemplateUsed(response, 'index_alumno.html')

    def test_template_registrar_admin_cuenta_responsable(self):
        self.deslogearse()
        self.logearseEncargado()
        respuesta = self.client.get(
            '/registro_de_administrador', {}, follow=True)
        self.assertTemplateNotUsed(respuesta, 'home_case.html')

    def test_template_registrar_admin_cuenta_alumno(self):
        self.deslogearse()
        self.logearseAlumno()
        respuesta = self.client.get(
            '/registro_de_administrador', {}, follow=True)
        self.assertTemplateNotUsed(respuesta, 'index_alumno.html')

    def test_error404_status(self):
        respuesta = self.client.get('/error404', {}, follow=True)
        self.assertEquals(respuesta.status_code, 200)

    def test_template_lista_adminisitradores_cuenta_encargado(self):
        self.deslogearse()
        self.logearseEncargado()
        response = self.client.get('/administradores', {}, follow=True)
        self.assertTemplateNotUsed(response, 'administradores.html')

    def test_template_lista_adminisitradores_cuenta_alumno(self):
        self.deslogearse()
        self.logearseAlumno()
        response = self.client.get('/administradores', {}, follow=True)
        self.assertTemplateNotUsed(response, 'administradores.html')

    def test_template_lista_alumnos_cuenta_alumno(self):
        self.deslogearse()
        self.logearseAlumno()
        response = self.client.get('/alumnos', {}, follow=True)
        self.assertTemplateNotUsed(response, 'alumnos.html')

    def test_template_lista_responsables_cuenta_encargado(self):
        self.deslogearse()
        self.logearseEncargado()
        response = self.client.get('/responsables', {}, follow=True)
        self.assertTemplateNotUsed(response, 'responsables.html')

    def test_template_lista_responsables_cuenta_alumno(self):
        self.deslogearse()
        self.logearseAlumno()
        response = self.client.get('/responsables', {}, follow=True)
        self.assertTemplateNotUsed(response, 'responsables.html')
        
    def test_template_home_cuenta_alumno(self):
        self.deslogearse()
        self.logearseAlumno()
        response = self.client.get('/home', {}, follow=True)
        self.assertTemplateNotUsed(response, 'home_case.html')
        
    def test_template_home_alumno_cuenta_admin(self):
        self.deslogearse()
        self.logearseAdmin()
        response = self.client.get('/home_alumno', {}, follow=True)
        self.assertTemplateNotUsed(response, 'home_alumno.html')
        
    def test_template_logout(self):
        self.deslogearse()
        self.logearseAdmin()
        response = self.client.get('/logout', {}, follow=True)
        self.assertTemplateUsed(response, 'login.html')
        
    def test_template_logout_alumno(self):
        self.deslogearse()
        self.logearseAlumno()
        response = self.client.get('/logout', {}, follow=True)
        self.assertTemplateUsed(response, 'login_alumno.html')

    def deslogearse(self):
        self.client.logout()

    def logearseAdmin(self):
        self.client.login(username='DanielAle', password='Ronaldinho999.')

    def logearseAlumno(self):
        self.client.login(username='12345678', password='Ronaldinho999.')

    def logearseEncargado(self):
        self.client.login(username='DanielCast', password='Ronaldinho999.')
