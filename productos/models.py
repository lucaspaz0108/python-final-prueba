from django.db import models

class Deporte(models.Model):
    nombre = models.CharField(max_length=50,unique=True)
    imagen = models.ImageField(upload_to="deportes",null=True,blank=True)

    def __str__(self):
        return f"{self.nombre}"

class Marca(models.Model):
    nombre = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return f"{self.nombre}"

class Articulo(models.Model):
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE,default=1)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2,max_digits=10)
    publicacion = models.DateField()
    imagen = models.ImageField(upload_to="articulos",null=True,blank=True)
