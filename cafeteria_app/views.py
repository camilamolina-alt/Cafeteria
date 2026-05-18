from django.shortcuts import render

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

def login(request):
    return render(request, 'cafeteria_app/login.html'),

def cart(request):
 return render(request, 'cafeteria_app/cart.html'),