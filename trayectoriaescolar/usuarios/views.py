from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import UserForm, AlumnoForm, ResponsableForm
from .models import Alumnos, Responsables
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

class BienvenidaView(LoginRequiredMixin, TemplateView):
    success_url = reverse_lazy('bienvenida')
    template_name = 'bienvenida.html'


class LoginView(LoginView):
    success_url = reverse_lazy('usuarios:home')
    template_name = 'login.html'
    form_class = AuthenticationForm
    


class LoginViewAlumno(LoginView):
    success_url = reverse_lazy('usuarios:home')
    template_name = 'login_alumno.html'
    form_class = AuthenticationForm 
    
    
@login_required
def home(request):
    return render(request, 'home_case.html')



@login_required
def homeAlumno(request):
    return render(request, 'index_alumno.html')


class RegistrarAdmin(CreateView):
    model = User
    form_class = UserForm
    template_name = 'registro_de_administrador.html'
    success_url = reverse_lazy('usuarios:login')
    success_message = "%(username)s se registró de manera exitosa"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('usuarios:login'))

@login_required   
def lista_admins(request):
    administradores = User.objects.filter(is_superuser=True)
    return render(request, 'administradores.html', {'administradores': administradores})

@login_required
def lista_alumnos(request):
    alumnos = User.objects.filter(is_superuser=False, is_staff=False)
    return render(request, 'alumnos.html', {'alumnos': alumnos})

class RegistrarAlumno(CreateView):
    model = Alumnos
    form_class = AlumnoForm
    template_name = 'registro_alumno.html'
    success_url = reverse_lazy('usuarios:home')
    #success_message = "%(matricula)s se registró de manera exitosa"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.is_superuser = False
        user.is_staff = False
        user.save()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('usuarios:home'))

class RegistrarResponsable(CreateView):
    model = Responsables
    form_class = ResponsableForm
    template_name = 'registro_responsable.html'
    success_url = reverse_lazy('usuarios:home')
    #success_message = "%(matricula)s se registró de manera exitosa"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.is_superuser = False
        user.is_staff = True
        user.save()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('usuarios:home'))

# Función para cerrar sesión.
@login_required
def signout(request):
    logout(request)
    return redirect('myLogin')
