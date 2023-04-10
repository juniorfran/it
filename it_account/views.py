from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.

def login_view(request):
    #si el usuario ya esta autenticado, redirige a la pagina
    if request.user.is_authenticated:
        return redirect('/app')
    
    #si no esta autenticado, redirige a la pagina de login
    if request.method == 'POST':
        #obtener los datos del formulario
        username = request.POST['username']
        password = request.POST['password']

        #Autenticar usuario
        user = authenticate(request, username=username, password=password)

        #si las credenciales son correctas
        if user is not None:
            #si el usuario esta registrado, lo loguea
            if user.is_active:
                login(request, user)
                return redirect('/app')
        else:
            #si las credenciales son incorrectas, mensaje de erros.
            message = 'Usuario o contraseña incorrectos'
            return render(request, 'account/login.html', {'message': message})
    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    return redirect('/app')