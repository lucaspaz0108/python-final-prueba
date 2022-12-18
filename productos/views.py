from django.shortcuts import render,redirect
from productos.models import *
from usuarios.models import *
from django.contrib.auth.decorators import login_required
from usuarios.views import avatar_usuario
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def inicio(request):
    deportes = Deporte.objects.all()
    contexto = {"avatar":avatar_usuario(request.user),"deporte_lista":deportes}
    return render(request,"productos/inicio.html",contexto)
    



@login_required
def articulos_listar(request,deporte_id):
    if deporte_id == "0":
        #obtengo el listado de articulos de la base de datos
        lista_articulos = Articulo.objects.all().order_by("nombre")
        deporte_elegido = "Todos"
    else:
        lista_articulos = Articulo.objects.filter(deporte=deporte_id).order_by("nombre")
        deporte_elegido = Deporte.objects.filter(id=deporte_id)[0].nombre
    contexto = {"avatar":avatar_usuario(request.user),"articulos_resultado":lista_articulos,"cantidad":len(lista_articulos),"deporte":deporte_elegido}
    return render(request,"productos/articulos_listar.html", contexto)

class DeportesList(ListView):

    model = Deporte
    template_name = "productos/deportes_listar.html"


def deportes_nuevo(request):
    if request.method == "POST":
        nombre_nuevo = request.POST["nombre"]
        imagen_nuevo = request.FILES["imagen"]
                
        deportes_nuevo = Deporte(nombre=nombre_nuevo, imagen=imagen_nuevo)
        deportes_nuevo.save() #con esto lo guardo en la base de datos
        return redirect("productos-inicio")
        
    return render(request, "productos/deportes_nuevo.html")

def deportes_eliminar(request, id_a_eliminar):
    deporte_borrar = Deporte.objects.get(id=id_a_eliminar)
    deporte_borrar.delete()

    return redirect("listar-deporte")

def articulo_nuevo(request):

    if request.method == "POST":
        deporte_nuevo = request.POST["deporte"]
        nombre_nuevo = request.POST["nombre"]
        marca_nuevo = request.POST["marca"]
        descripcion_nuevo = request.POST["descripcion"]
        precio_nuevo = request.POST["precio"]
        publicacion_nuevo = request.POST["publicacion"]
        imagen_nuevo = request.FILES["imagen"]

        deporte_instancia = Deporte.objects.filter(nombre=deporte_nuevo)[0]
        marca_instancia = Marca.objects.filter(nombre=marca_nuevo)[0]

        articulo_nuevo = Articulo(deporte=deporte_instancia, nombre=nombre_nuevo,marca=marca_instancia, descripcion=descripcion_nuevo, precio=precio_nuevo, publicacion=publicacion_nuevo, imagen=imagen_nuevo)
        articulo_nuevo.save() #con esto lo guardo en la base de datos
        return redirect("productos-inicio")

    marcas = Marca.objects.all()
    deportes = Deporte.objects.all()
    return render(request, "productos/articulo_nuevo.html",{"marcas":marcas,"deportes":deportes})

def articulos_eliminar(request, id_a_eliminar):
    articulo_borrar = Articulo.objects.get(id=id_a_eliminar)
    articulo_borrar.delete()

    return redirect("productos-inicio")

def articulos_editar(request, id_a_editar):
    articulo_editar = Articulo.objects.get(id=id_a_editar)

    if request.method == "POST":
        articulo_editar.nombre = request.POST["nombre"]
        articulo_editar.descripcion = request.POST["descripcion"]
        articulo_editar.precio = request.POST["precio"]
        articulo_editar.publicacion = request.POST["publicacion"]
        
        articulo_editar.save() #con esto guardo los cambios en la base de datos
        return redirect("productos-inicio")
    else:
        datos_inicio = {"inicial":articulo_editar}
        return render (request,"productos/articulo_editar.html",datos_inicio)

def articulos_detalle(request,id_detalle):
    articulo_detalle = Articulo.objects.get(id=id_detalle)
    
    if request.method == "POST":
        mensaje = Mensajes(user_id=request.user.id, articulo_id=id_detalle, mensaje=request.POST["mensaje"])
        mensaje.save()
        
    
    mensajes_articulo = Mensajes.objects.filter(articulo_id=id_detalle)
    
    return render(request, "productos/articulo_detalle.html",{"articulo":articulo_detalle,"mensajes":mensajes_articulo})
    
def sobre_nosotros(request):
    return render(request, "productos/sobre_nosotros.html")