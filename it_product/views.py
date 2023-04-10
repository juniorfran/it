from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Productos


# Create your views here.

@login_required
def product_list(request):
    """
    Lista de productos
    """
    productos = Productos.objects.all()
    return render(request, 'product/product_list.html', {'productos': productos})


@login_required
def product_create(request):
    """
    Crea un producto
    """
    suc_empresas = Productos.objects.all()

    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        stock = request.POST['stock']
        serie = request.POST['serie']
        descripcion = request.POST['descripcion']
        ubicacion = request.POST['ubicacion']
        imagen = request.POST['imagen']
        
        producto = Productos(nombre=nombre, precio=precio, stock=stock, serie=serie, descripcion=descripcion,
                             ubicacion=ubicacion, imagen=imagen)
        producto.save()
        return redirect('product_list')
    else:
        
        return render(request, 'product/product_create.html', {'suc_empresas':suc_empresas})

def suc_empresa_submission(request):
    """
    Subida de un producto
    """
    suc_empresa_pk = request.POST.get('suc_empresa')
    suc_empresa = Productos.objects.get(pk=suc_empresa_pk)
    suc_emp = Productos(suc_empresa=suc_empresa)
    suc_emp.save()
    return redirect('product_list')


@login_required
def product_edit(request, pk):
    """
    Edita un producto
    """
    producto = get_object_or_404(Productos, pk=pk)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.serie = request.POST['serie']
        producto.descripcion = request.POST['descripcion']
        producto.ubicacion = request.POST['ubicacion']
        producto.save()
        return redirect('product_list')
    else:
        return render(request, 'product/product_edit.html', {'producto': producto})


@login_required
def product_delete(request, pk):
    """
    Elimina un producto
    """
    producto = get_object_or_404(Productos, pk=pk)
    producto.delete()
    return redirect('product_list')
