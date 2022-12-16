from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Correo electrónico")
    password1: forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2: forms.CharField(label="Confirme contraseña", widget=forms.PasswordInput)

    #django trae una clase que sirve para configurar el formulario
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]
        #Sacamos los mensajes de ayuda
        help_texts = { "email": "Indica un correo electronico que uses habitualmente", "first_name": "", "last_name": "", "password1": ""}

class UserEditForm(UserChangeForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Correo electrónico")

    class Meta:
        model = User
        fields = ["first_name","last_name","email"]
        help_texts = { "email": "Indica un correo electronico que uses habitualmente", "first_name": "", "last_name": ""}
   