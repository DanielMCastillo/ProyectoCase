from django.urls import path
# from articulos import views, views_categoria
from usuarios import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('', views.BienvenidaView.as_view(), name='bienvenida'),
    path('administradores', views.lista_admins, name='administradores'),
    path('salir', LogoutView.as_view(), name='logout'),
    path('registro_de_administrador', views.RegistrarAdmin.as_view(), name='registro_de_administrador'),
    

]
