from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate #funcines necesarias
from django.contrib.auth.forms import AuthenticationForm
from usuarios.forms import UserRegisterForm, UserEditForm, AvatarForm
from usuarios.models import *
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# importo el paquete os para manejar nombres de archivo
import os

#Defino la función para iniciar sesión
def iniciar_sesion(request):

    errors = ""

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST) #así me lo pide el formulario de django (AuthenticationForm)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"]) #la función autehenticate devuelve un objeto de la clase "user" o un None

            #si el usuario existe
            if user is not None: 
                #vamos a hacer el login
                login(request, user) 
                return redirect("productos-inicio")
            
            #si el usuario NO existe
            else:
                return render(request, "usuarios/login.html", {"form":formulario, "errors": "Credenciales no validas"})
        else:
            return render(request, "usuarios/login.html", {"form":formulario, "errors": formulario.errors})
    
    formulario = AuthenticationForm()
    return render(request, "usuarios/login.html", {"form":formulario, "errors":errors})

#Creamos una vista para el registro de un usuario nuevo
def registrar_usuario(request):
    errors = ""
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            formulario.save()
            user = authenticate(username=data["username"], password=data["password1"])
            login(request,user)
            return redirect("productos-inicio")
        else:
            return render(request,"usuarios/registrar_usuario.html", {"form":formulario, "errors": errors})
            
    formulario = UserRegisterForm()
    return render(request, "usuarios/registrar_usuario.html", {"form":formulario, "errors": errors})

@login_required
def editar_usuario(request):
    
    usuario = request.user
    if request.method == "POST":
        formulario = UserEditForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            #usuario.password1 = data["password1"]
            #usuario.password2 = data["password2"]
            usuario.save()

            return redirect("productos-inicio")
    else:
        formulario = UserEditForm(initial={"first_name":usuario.first_name,"last_name":usuario.last_name,"email":usuario.email})

    return render(request,"usuarios/editar_usuario.html", {"form":formulario,"usuario":usuario})
    
def avatar_usuario(u_activo):

    if u_activo.is_authenticated:
        if len(Avatar.objects.filter(user= u_activo.id))==1:
            imagen_model = Avatar.objects.filter(user= u_activo.id)[0]
            imagen_url = imagen_model.imagen.url
        else:
            imagen_url=""
    else:
        imagen_url = ""
    return (imagen_url)
    

    
