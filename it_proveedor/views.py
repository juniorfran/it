from django.shortcuts import redirect, render
from .models import Empresas, Suc_Empresa, Representante

def emmpresa_create(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        nit = request.POST['nit']
        nrc = request.POST['nrc']
        pagina_web = request.POST['pagina_web']
        telefono = request.POST['telefono']
        email = request.POST['email']
        #representante = request.POST['representante']
        empresa = Empresas(nombre=nombre, direccion=direccion, nit=nit, nrc=nrc, pagina_web=pagina_web, telefono=telefono, email=email)
        empresa.save()
        return redirect('empresas:empresas')
    else:
        return render(request, 'empresas/empresas.html')

def empresa_list(request):
    empresas = Empresas.objects.all()
    return render(request, 'empresas/empresas_list.html', {'empresas':empresas})

def empresa_update(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        nit = request.POST['nit']
        nrc = request.POST['nrc']
        pagina_web = request.POST['pagina_web']
        telefono = request.POST['telefono']
        email = request.POST['email']
        #representante = request.POST['representante']
        id = request.POST['id']
        empresa = Empresas.objects.get(id=id)
        empresa.nombre = nombre
        empresa.direccion = direccion
        empresa.nit = nit
        empresa.nrc = nrc
        empresa.pagina_web = pagina_web
        empresa.telefono = telefono
        empresa.email = email
        empresa.save()
        return redirect('empresas:empresas')
    else:
        return render(request, 'empresas/empresas.html')

def empresa_delete(request):
    if request.method == 'POST':
        id = request.POST['id']
        empresa = Empresas.objects.get(id=id)
        empresa.delete()
        return redirect('empresas:empresas')
    else:
        return render(request, 'empresas/empresas.html')
    

def empresa_shear(request):
    if request.method == 'POST':
        id = request.POST['id']
        empresa = Empresas.objects.get(id=id)
        empresa.shear()
        return redirect('empresas:empresas')
    else:
        return render(request, 'empresas/empresas.html')

        

# Create your views here.
