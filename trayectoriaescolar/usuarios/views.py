from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

class BienvenidaView(LoginRequiredMixin, TemplateView):
    success_url = reverse_lazy('bienvenida')
    template_name = 'bienvenida.html'


class LoginView(LoginView):
    success_url = reverse_lazy('index_case.html')
    template_name = 'login.html'
    form_class = AuthenticationForm


class RegistrarAdmin(CreateView):
    model = User
    form_class = UserForm
    template_name = 'registro_de_administrador.html'
    success_url = reverse_lazy('usuarios:login')
    success_message = "%(username)s se registró de manera exitosa"


def lista_admins(request):
    administradores = User.objects.all()
    return render(request, 'administradores.html', {'administradores': administradores})



# Función para cerrar sesión.
@login_required
def signout(request):
    logout(request)
    return redirect('myLogin')
