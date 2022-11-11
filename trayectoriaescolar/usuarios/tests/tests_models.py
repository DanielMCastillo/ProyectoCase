from django.test import SimpleTestCase, TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from usuarios.forms import UserForm

class TestModelsUsuarios(TestCase):
    
    def setUp(self):
        usuario = User.objects.create(
            username = 'jesus',
            #password= 'jesus123'
        )
        usuario.set_password('jesus123')
        usuario.is_superuser = True
        usuario.is_active = True
        usuario.is_staff = True
        usuario.save()
        
    def test_template_registro(self):
        respuesta = self.client.get('/registro')
        self.assertAlmostEquals(respuesta.status_code,200)
        
    def test_template_nuevo_usuario(self):
        respuesta = self.client.get('/registro')
        self.assertAlmostEquals(respuesta.status_code,200)
    
    def test_template_login(self):
        respuesta = self.client.get('/entrar')
        self.assertAlmostEqual(respuesta.status_code,200)