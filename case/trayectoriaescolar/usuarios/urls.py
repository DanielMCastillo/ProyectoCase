from django.urls import path
# from articulos import views, views_categoria
from usuarios import views
from django.contrib.auth.views import LogoutView, LoginView

app_name = 'usuarios'

urlpatterns = [
    path('', views.BienvenidaView.as_view(), name='bienvenida'),
    path('salir', LogoutView.as_view(), name='logout'),
    path('entrar', LoginView.as_view(), name='login'),
    path('registrar', views.RegistrarAdmin.as_view(), name='registrar'),
    #path('lista', views.ListaUsuariosView.as_view(), name='lista'),
]