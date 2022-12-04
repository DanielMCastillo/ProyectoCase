from django.urls import path
from usuarios.views import RegistrarAlumno
# from articulos import views, views_categoria
from usuarios import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('login', views.LoginView.as_view(), name='login'),
    path('', views.LoginViewAlumno.as_view(), name='login_alumno'),
    path('administradores', views.lista_admins, name='administradores'),
    path('alumnos', views.lista_alumnos, name='alumnos'),
    path('responsables', views.lista_responsables, name='responsables'),
    path('salir', LogoutView.as_view(), name='logout'),
    path('registro_de_administrador', views.RegistrarAdmin.as_view(), name='registro_de_administrador'),
    path('registro_alumno', views.RegistrarAlumno.as_view(), name='registro_alumno'),
    path('home_case', views.home, name='home'),
    path('home_alumno', views.homeAlumno, name='home_alumno'),
    path('registro_responsable', views.RegistrarResponsable.as_view(), name='registro_responsable'),
    path('error404', views.error404, name='error404'),
    


]
