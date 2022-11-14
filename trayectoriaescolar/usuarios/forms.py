from django import forms
from usuarios.models import Administradores


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
        if not any(chr.isalpha() for chr in contrasena1):
            raise forms.ValidationError(
                'La contraseña debe contener al menos una letra')
        if contrasena1.islower():
            raise forms.ValidationError(
                'La contraseña debe contener al menos una letra mayuscula')
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
