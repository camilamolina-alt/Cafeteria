from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

def ejemplo(request):
    return render(request, 'cafeteria_app/ejemplo.html') #Ejemplos para prueas de vistas random

def home(request):
    return render(request, 'cafeteria_app/index.html')

def shop(request):
    return render(request, 'cafeteria_app/shop.html')

def menu(request):
    return render(request, 'cafeteria_app/menu.html')

def gallery(request):
    return render(request, 'cafeteria_app/gallery.html')


def events(request):
    return render(request, 'cafeteria_app/events.html')

@login_required
def cart(request):
    return render(request, 'cafeteria_app/cart.html')

def registro(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html',{
            'form': UserCreationForm()
        })
    else:
        if request.POST['password1']==request.POST['password2']:
            #registrar usuario
            try:
                user =User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse('Usuario registrado exitosamente')
            except:
                return render(request, 'registration/register.html',{
                    'form': UserCreationForm(),
                    "error": 'El nombre de usuario ya existe'
                })
        return render(request, 'registration/register.html',{
                    'form': UserCreationForm(),
                    "error": 'contraseñas no coinciden'
                })
        

def exit(request):
    logout(request)
    return redirect('index')