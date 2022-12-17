from django.urls import path
from productos.views import *

urlpatterns = [
    path("inicio/", inicio, name="productos-inicio"),
    #path("admin/inicio/", admin_inicio, name="admin-inicio"),
    #path("nuevo_deporte/",deportes_nuevo,name="deportes-nuevo"),
    path("nuevo_articulo/",articulo_nuevo,name="articulo-nuevo"),
    path("articulos_listar/<deporte_id>/",articulos_listar,name="articulos-listar"),
    path("articulos_eliminar/<id_a_eliminar>/",articulos_eliminar,name="articulos-eliminar"),
    path("articulos_editar/<id_a_editar>/",articulos_editar,name="articulos-editar"),
    path("articulos_detalle/<id_detalle>/",articulos_detalle,name="articulos-detalle")
]