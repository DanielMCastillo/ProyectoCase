from django.urls import path
# from articulos import views, views_categoria
from usuarios import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('', views.BienvenidaView.as_view(), name='bienvenida'),
    
    path('administrador', views.lista_admins, name='administradores'),
    path('salir', LogoutView.as_view(), name='logout'),
    path('entrar', views.LoginView.as_view(), name='login'),
    #path('entrar', views.loginView, name='login'),
    path('registrar', views.RegistrarAdmin.as_view(), name='registrar'),
    #path('lista', views.ListaUsuariosView.as_view(), name='lista'),
]