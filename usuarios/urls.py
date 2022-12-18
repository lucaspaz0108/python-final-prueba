from django.urls import path
from usuarios.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", iniciar_sesion, name="usuarios-login"),
    path("registrar/", registrar_usuario, name="usuarios-registrar"),
    path("editar/", editar_usuario, name="usuarios-editar"),
    path("logout/", LogoutView.as_view(template_name="usuarios/logout.html"), name="usuarios-logout"),
    path("agregar_avatar/", avatar_usuario, name="agregar-avatar")
]