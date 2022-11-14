from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import UserForm


class BienvenidaView(LoginRequiredMixin, TemplateView):
    success_url = reverse_lazy('bienvenida')
    template_name = 'bienvenida.html'


class LoginView(LoginView):
    success_url = reverse_lazy('bienvenida')
    template_name = 'login.html'
    form_class = AuthenticationForm


class RegistrarAdmin(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('usuarios:login')
    success_message = "%(username)s se registró de manera exitosa"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return super().form_valid(form)


def lista_admins(request):
    administradores = User.objects.all()
    return render(request, 'administradores.html', {'administradores': administradores})
