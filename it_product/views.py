from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from .models import Productos
from it_proveedor.models import Suc_Empresa
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry
# from django_datatables_view.base_datatable_view import BaseDatatableView
from django.views.decorators.http import require_http_methods



# Create your views here.

def inst_suc_empresas(request):
    """
    """
    suc_empresas = Suc_Empresa.objects.all()
    return render(request, 'product/product_create.html', {'suc_empresas': suc_empresas})

@login_required
def product_list(request, id):
    """
    Lista de productos
    """
    # productos = Productos.objects.all()
    # paginator = Paginator(productos, 10)
    # page_number = request.GET.get('page')
    # page_object = paginator.get_page(page_number)

    productos = Productos.objects.get(pk=id)
    content_type = ContentType.objects.get_for_model(productos)
    

    paginator = Paginator(Productos.objects.all(), 2)
    page_number = request.GET.get('page')
    try:
        page_object = paginator.get_page(page_number)
        cambios = LogEntry.objects.filter(
        content_type=content_type,
        object_id=productos.id
    )
    except:
        page_object = paginator.get_page(1)
        return render(request, 'product/product_list.html', {
            'productos': productos,
            'cambios': cambios,
            'page_object': page_object
            })
    return render(request, 'product/product_list.html', {'page_object': page_object})

@login_required
def historial_cambios(request, id):
    """
    """
    productos = Productos.objects.get(pk=id)
    content_type = ContentType.objects.get_for_model(productos)
    cambios = LogEntry.objects.filter(
        content_type=content_type,
        object_id=productos.id
        )
    return render(request, 'product/historial_cambios.html', {

        'cambios': cambios
        })



# @login_required
def product_view(request):
    """
    vista de suc_empresa ID
    """
    suc_empresas = Suc_Empresa.objects.all()
    return render(request, 'product/product_create.html', {'suc_empresas': suc_empresas})
pass

# @require_http_methods(["GET", "POST"])
# @login_required
# def tabla_lista_produtos(request):
#     datos = Productos.objects.all()
#     paginator = Paginator(datos, 2)
#     page = request.GET.get('page')

#     try:
#         page_object = paginator.get_page(page)
#     except PageNotAnInteger:
#         page_object = paginator.get_page(1)
#     except EmptyPage:
#         page_object = paginator.get_page(paginator.num_pages)
#     return render(request, 'product/product_create.html', {'page_object': page_object})
# pass

def mi_vista(request):
    datos = Productos.objects.all()

    # Crea un objeto Paginator con los datos y el tamaño de página deseado
    paginator = Paginator(datos, 10)

    # Obtiene el número de página actual de la solicitud GET
    page = request.GET.get('page')

    try:
        # Obtiene la página solicitada
        paginado = paginator.page(page)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página
        paginado = paginator.page(1)
    except EmptyPage:
        # Si el número de página es mayor que el número de páginas, muestra la última página
        paginado = paginator.page(paginator.num_pages)

    # Renderiza la plantilla con los datos paginados
    return render(request, 'product/product_create.html', {'datos': paginado})

@require_http_methods(["GET", "POST"])
@login_required
def product_create(request):
    """
    Crea un producto
    """

    
    suc_empresas = Productos.objects.all()

    datos = Productos.objects.all()

    # Crea un objeto Paginator con los datos y el tamaño de página deseado
    paginator = Paginator(datos, 2)

    # Obtiene el número de página actual de la solicitud GET
    page = request.GET.get('page')

    try:
        paginado = paginator.page(page)
        if request.method == 'POST':
            
            nombre = request.POST['nombre']
            precio = request.POST['precio']
            stock = request.POST['stock']
            serie = request.POST['serie']
            descripcion = request.POST['descripcion']
            ubicacion = request.POST['ubicacion']
            imagen = request.POST['imagen']
            suc_empresa_id = request.POST['suc_empresa'] #el ID de la sucursal de la empresa
            suc_empresa = Suc_Empresa.objects.get(id=suc_empresa_id) #instanciamos el id y lo igualamos con el seleccionado
            
            producto = Productos(nombre=nombre, precio=precio, stock=stock, serie=serie, descripcion=descripcion,
                                ubicacion=ubicacion, imagen=imagen, suc_empresa=suc_empresa)
            producto.save()
            SUCCESS = 25
            messages.add_message(request, SUCCESS, "Se guardo el producto")
            return redirect('product_create')
        else:
            #diccionario para las instanacias de objetos.
            
            #dic = {
            #    'suc_empresas': Suc_Empresa.objects.all()
            #}
            # paginator = Paginator(Productos.objects.all(), 10)
            # page_number = request.GET.get('page')
            # page_object = paginator.get_page(page_number) 
            return render(request, 'product/product_create.html', {'dic':dic})
        
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página
        paginado = paginator.page(1)
    except EmptyPage:
        # Si el número de página es mayor que el número de páginas, muestra la última página
        paginado = paginator.page(paginator.num_pages)
    # except:
    #     return redirect('product_create')
        # return render(request, 'product/product_create.html', {'page_object': page_object}) 

    return render(request, 'product/product_create.html', {'datos': paginado, 'suc_empresas':suc_empresas})


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
