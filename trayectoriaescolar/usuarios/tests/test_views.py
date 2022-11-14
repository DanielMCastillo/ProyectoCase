from django.test import TestCase
from django.contrib.auth.models import User

class TestViewsCase(TestCase):
    def setUp(self):
        usuario = User(
            username='amcdanymx',
            password='Ronaldinho999.',
            is_superuser=True,
            is_active=True,
            is_staff=True
        )
        usuario.set_password('Ronaldinho999.')
        usuario.save()
        self.client.login(username='amcdanymx', password='Ronaldinho999.')

    def test_login_estatus(self):
        respuesta = self.client.get('/entrar', {}, follow=True)
        self.assertEquals(respuesta.status_code, 200)

    def test_registrar_estatus(self):
        respuesta = self.client.get('/registrar', {}, follow=True)
        self.assertEquals(respuesta.status_code, 200)
        
    def test_bienvenida_estatus(self):
        respuesta = self.client.get('', {}, follow=True)
        self.assertEquals(respuesta.status_code, 200)

    def test_adminisitradores_estatus(self):
        respuesta = self.client.get('/administradores', {}, follow=True)
        self.assertEquals(respuesta.status_code, 200)
    
    def test_template_admin_nuevo(self):
        response = self.client.get('/registrar')
        self.assertTemplateUsed(response, 'auth/user_form.html')
    
    def test_template_login(self):
        response = self.client.get('/entrar')
        self.assertTemplateUsed(response, 'login.html')
