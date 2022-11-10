from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Create your views here.

class BienvenidaView(LoginRequiredMixin, TemplateView):
    template_name = 'bienvenida.html'
    
class LoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('bienvenida')
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