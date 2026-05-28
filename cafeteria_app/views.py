from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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
    error = False
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not username or not password:
            error = True
    return render(request, 'registration/login.html', {'error': error})

@login_required
def cart(request):
    return render(request, 'cafeteria_app/cart.html')