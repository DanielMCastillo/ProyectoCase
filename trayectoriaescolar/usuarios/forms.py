from django import forms
from usuarios.models import Administradores, Alumnos, Responsables


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
        fields = ('username', 'email', 'nombre', 'nombre2', 'apellidoP', 'apellidoM', 'telefono', 'password', 'repassword')
    email = forms.EmailField(required=True)
    
    def save(self, commit=True):
        user = super(AlumnoForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        
        if commit:
            user.save()
        return user
    
    def clean_username(self):
        matric = self.cleaned_data['username']
        if len(matric) < 8 or len(matric) > 8:
            raise forms.ValidationError(
                'La matrícula debe contener exactamente 8 dígitos')
        if self.esNumero(matric) == False:
            raise forms.ValidationError(
                'La matrícula debe contener solo números'
            )
        return matric
    
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
    
    def clean_telefono(self):
        tel = self.cleaned_data['telefono']
        if tel != None:
            if self.esNumero(tel) == False:
                raise forms.ValidationError(
                    'El telefono debe ser un número'
                )
            if len(tel) != 10:
                raise forms.ValidationError(
                    'El telefono debe ser un número de 10 dígitos'
                )

    def esNumero(self, num):
        try:
            int(num)
            return True
        except:
            return False
    
class FormAlumnos(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = '__all__'
        widgets = {
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre2': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidoP': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidoM': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class ResponsableForm(forms.ModelForm):
    repassword = forms.CharField()

    class Meta:
        model = Responsables
        fields = ('username', 'email', 'nombre', 'nombre2', 'apellidoP', 'apellidoM', 'programa_academico', 'unidad_academica', 'password', 'repassword')

    email = forms.EmailField(required=True)

    def save(self, commit=True):
        user = super(ResponsableForm, self).save(commit=False)
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
    
class FormResponsables(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = '__all__'
        widgets = {
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre2': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidoP': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidoM': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad_academica': forms.TextInput(attrs={'class': 'form-control'}),
            'programa_academico': forms.TextInput(attrs={'class': 'form-control'}),
        }