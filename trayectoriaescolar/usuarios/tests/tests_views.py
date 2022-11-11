from django.test import SimpleTestCase, TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from usuarios.forms import UserForm

class TestViewsUsuarios(TestCase):
    
    def setUp(self):
        usuario = User.objects.create(
            username = 'jesusjuarez',
            #password= 'jesus123'
        )
        usuario.set_password('Jesus.123')
        usuario.is_superuser = True
        usuario.is_active = True
        usuario.is_staff = True
        usuario.save()
        
        self.client.login(username = 'jesusjuarez', password= 'Jesus.123')
        
    def test_template_login(self):
        respuesta = self.client.get('/entrar')
        self.assertAlmostEquals(respuesta.status_code,200)
        
    def test_template_administradores(self):
        respuesta = self.client.get('/administradores')
        self.assertAlmostEquals(respuesta.status_code,200)
        
    def test_template_nuevo_usuario(self):
        respuesta = self.client.get('/registrar')
        self.assertAlmostEquals(respuesta.status_code,200)