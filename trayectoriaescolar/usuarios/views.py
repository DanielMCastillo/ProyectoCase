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
from .models import Administradores, Alumnos, Responsables
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from tkinter import messagebox as MessageBox


class BienvenidaView(LoginRequiredMixin, TemplateView):
    success_url = reverse_lazy('bienvenida')
    template_name = 'bienvenida.html'


class LoginView(LoginView):
    success_url = reverse_lazy('usuarios:home')
    template_name = 'login.html'
    form_class = AuthenticationForm


class LoginViewAlumno(LoginView):
    success_url = reverse_lazy('home_alumno')
    template_name = 'login_alumno.html'
    form_class = AuthenticationForm


@login_required
def home(request):
    if request.user.is_staff:
        return render(request, 'home_case.html')
    else:
        return redirect('usuarios:home_alumno')


@login_required
def homeAlumno(request):
    if request.user.is_superuser == False and request.user.is_staff == False:
        return render(request, 'index_alumno.html')
    else:
        return redirect('usuarios:home')


def error404(request):
    return render(request, '404.html')


class RegistrarAdmin(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'registro_de_administrador.html'
    success_url = reverse_lazy('usuarios:login')
    success_message = "%(username)s se registró de manera exitosa"

    # def permiso(self):
    #    if not self.request.user.is_superuser:
    #        if self.request.user.is_staff:
    #            return redirect('usuarios:home')
    #        else:
    #            return redirect('usuarios:home_alumno')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('usuarios:login'))


class RegistrarAdminCASE(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'registro_admin_case.html'
    success_url = reverse_lazy('usuarios:home')
    success_message = "%(username)s se registró de manera exitosa"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('usuarios:home'))


@login_required
def lista_admins(request):
    if request.user.is_superuser:
        administradores = User.objects.filter(is_superuser=True)
        return render(request, 'administradores.html', {'administradores': administradores})
    else:
        if request.user.is_staff:
            return redirect('usuarios:home')
        else:
            return redirect('usuarios:home_alumno')


@login_required
def lista_alumnos(request):
    if not request.user.is_staff:
        return redirect('usuarios:home_alumno')
    user_alumno = Alumnos.objects.all()
    return render(request, 'alumnos.html', {'alumnos': user_alumno})


@login_required
def lista_responsables(request):
    if request.user.is_superuser:
        user_responsable = Responsables.objects.all()
        return render(request, 'responsables.html', {'responsables': user_responsable})
    else:
        if request.user.is_staff:
            return redirect('usuarios:home')
        else:
            return redirect('usuarios_home_alumno')


class RegistrarAlumno(LoginRequiredMixin, CreateView):
    model = Alumnos
    form_class = AlumnoForm
    template_name = 'registro_alumno.html'
    success_url = reverse_lazy('usuarios:home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.is_superuser = False
        user.is_staff = False
        user.save()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('usuarios:home'))


class RegistrarResponsable(LoginRequiredMixin, CreateView):
    model = Responsables
    form_class = ResponsableForm
    template_name = 'registro_responsable.html'
    success_url = reverse_lazy('usuarios:home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.is_superuser = False
        user.is_staff = True
        user.save()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('usuarios:home'))

# Función para cerrar sesión/SI SE OCUPA NO BORRAR


@login_required
def signout(request):
    logout(request)
    return redirect('usuarios:login')

# Función para cerrar sesión/SI SE OCUPA NO BORRAR


@login_required
def signoutAlumno(request):
    logout(request)
    return redirect('usuarios:login_alumno')
