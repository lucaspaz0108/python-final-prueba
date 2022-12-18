from django.urls import path
from productos.views import *

urlpatterns = [
    path("inicio/", inicio, name="productos-inicio"),
    #path("admin/inicio/", admin_inicio, name="admin-inicio"),
    path("nuevo_deporte/",deportes_nuevo,name="deportes-nuevo"),
    path("deporte_listar/", DeportesList.as_view(),name="listar-deporte"),
    #path("deporte_listar/", deportes_listar,name="listar-deporte"),
    path("deporte_eliminar/<id_a_eliminar>/", deportes_eliminar,name="eliminar-deporte"),
    path("nuevo_articulo/",articulo_nuevo,name="articulo-nuevo"),
    path("articulos_listar/<deporte_id>/",articulos_listar,name="articulos-listar"),
    path("articulos_eliminar/<id_a_eliminar>/",articulos_eliminar,name="articulos-eliminar"),
    path("articulos_editar/<id_a_editar>/",articulos_editar,name="articulos-editar"),
    path("articulos_detalle/<id_detalle>/",articulos_detalle,name="articulos-detalle"),
    path("sobre_nosotros/", sobre_nosotros,name="sobre-nosotros"),
]