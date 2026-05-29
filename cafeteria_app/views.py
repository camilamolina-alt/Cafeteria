from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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

def exit(request):
    logout(request)
    return redirect('index')