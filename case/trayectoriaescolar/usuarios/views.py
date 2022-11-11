from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import UserForm

# Create your views here.

#def bienvenidaView(request):
#    return render(request, 'bienvenida.html')
class BienvenidaView(LoginRequiredMixin, TemplateView):
    template_name = 'bienvenida.html'
   
class LoginView(LoginView):
    success_url = reverse_lazy('administradores')
    template_name = 'login.html'
    form_class = AuthenticationForm

#def loginView(request):
#    if request.method == 'GET':
#        return render(request, 'login.html', {"form": AuthenticationForm})
#    else:
#        user = authenticate(
#            request, username=request.POST['username'], password=request.POST['password'])
#        if user is None:
#           return render(request, 'login.html', {"form": AuthenticationForm, "error": "Usuario o contraseña incorrectos."})
#
#        login(request, user)
#        return redirect('administradores')
    #template_name = 'login.html'
    #form_class = AuthenticationForm

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