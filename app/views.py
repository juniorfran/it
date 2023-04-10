from django.shortcuts import render

from it_product.models import Productos

# Create your views here.

def index(request):
    """
    Lista de productos
    """
    productos = Productos.objects.all()
    return render(request, 'app/home.html', {'productos': productos})
