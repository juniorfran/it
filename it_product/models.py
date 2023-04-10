from django.db import models
from it_proveedor.models import Suc_Empresa, Representante, Empresas 

# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    stock = models.CharField(max_length=50)
    serie = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='static/upload')
    suc_empresa = models.ForeignKey(Suc_Empresa, on_delete=models.CASCADE, default='1')
    #sucursal = models.ForeignKey("it_sucursal.Sucursales", on_delete=models.CASCADE)


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)


