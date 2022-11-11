from django.test import SimpleTestCase, TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from usuarios.forms import UserForm

class TestViewsUsuarios(TestCase):
    
    def setUp(self):
        usuario = User.objects.create(
            username = 'jesus',
            #password= 'jesus123'
        )
        usuario.set_password('jesus123')
        usuario.save()
        
        self.client.login(username = 'jesus', password= 'jesus123')
        
    def test_template_login(self):
        respuesta = self.client.get('/login')
        self.assertAlmostEquals(respuesta.status_code,200)
        
    def test_template_administradores(self):
        respuesta = self.client.get('/administradores')
        self.assertAlmostEquals(respuesta.status_code,200)
        
    def test_template_nuevo_usuario(self):
        respuesta = self.client.get('/registro')
        self.assertAlmostEquals(respuesta.status_code,200)