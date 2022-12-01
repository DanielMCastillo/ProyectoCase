from django import forms
from usuarios.models import Administradores, Alumnos


class UserForm(forms.ModelForm):
    repassword = forms.CharField()

    class Meta:
        model = Administradores
        fields = ('username', 'email', 'password', 'repassword')

    email = forms.EmailField(required=True)

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def clean_password(self, *args, **kwargs):
        contrasena1 = self.data['password']
        contrasena2 = self.data['repassword']
        if len(contrasena1) < 8:
            raise forms.ValidationError(
                'La contraseña debe contener al menos 8 caracteres')
        if contrasena1.islower():
            raise forms.ValidationError(
                'La contraseña debe contener al menos una letra mayuscula')
        if not any(chr.isalpha() for chr in contrasena1):
            raise forms.ValidationError(
                'La contraseña debe contener al menos una letra')
        if contrasena1.isupper():
            raise forms.ValidationError(
                'La contraseña debe contener al menos una letra minuscula')
        if contrasena1.isalnum():
            raise forms.ValidationError(
                'La contraseña debe contener al menos un caracter especial')
        if not any(chr.isdigit() for chr in contrasena1):
            raise forms.ValidationError(
                'La contraseña debe contener al menos un número')
        if contrasena1 != contrasena2:
            raise forms.ValidationError('Las contraseñas son diferentes')

        return self.data['password']

    def clean_username(self):
        usern = self.cleaned_data['username']
        if len(usern) < 8:
            raise forms.ValidationError(
                'El usuario debe contener 8 o mas caracteres')
        if ' ' in usern:
            raise forms.ValidationError(
                'El nombre de usuario no debe contener espacios')
        if not usern.isalnum():
            raise forms.ValidationError(
                'El nombre de usuario no debe contener caracteres especiales')
        return usern


class FormAdmins(forms.ModelForm):
    class Meta:
        model = Administradores
        fields = '__all__'
        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AlumnoForm(forms.ModelForm):
    repassword = forms.CharField()
    class Meta:
        model = Alumnos
        fields = ('matricula', 'email', 'nombre', 'nombre2', 'apellidoP', 'apellidoM', 'telefono')
    email = forms.EmailField(required=True)
    
    def save(self, commit=True):
        user = super(AlumnoForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
    def clean_matricula(self):
        matric = self.cleaned_data['matricula']
        if isinstance(matric,int) == False:
            raise forms.ValidationError(
                'La matrícula debe contener solo números'
            )
        if len(matric) < 8 or len(matric) > 8:
            raise forms.ValidationError(
                'La matrícula debe contener exactamente 8 dígitos')
        alumnos = Alumnos.objects.all()
        for alumno in alumnos:
            if alumno[0] == matric:
                raise forms.ValidationError(
                    'Esta matrícula ya esta registrada'
                )
        return matric
    
    def clean_nombre(self):
        nom = self.cleaned_data['nombre']
        if nom == '' or nom == ' ':
            raise forms.ValidationError(
                'El nombre no puede estar vacío'
            )
        return nom
            
    def clean_apellidoP(self):
        apep = self.cleaned_data['apellidoP']
        if apep == '' or apep == ' ':
            raise forms.ValidationError(
                'El primer apellido no puede estar vacío'
            )
        return apep
    
    def clean_apellidoM(self):
        apem = self.cleaned_data['apellidoM']
        if apem == '' or apem == ' ':
            raise forms.ValidationError(
                'El segundo apellido no puede estar vacío'
            )
        return apem
    
    def clean_telefono(self):
        tel = self.cleaned_data['telefono']
        if len(tel) != 0:
            if isinstance(tel,int) == False:
                raise forms.ValidationError(
                    'El telefono debe ser un número'
                )
            if len(tel) != 10:
                raise forms.ValidationError(
                    'El telefono debe ser un número de 10 dígitos'
                )
                
class FormAlumnos(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = '__all__'
        widgets = {
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }