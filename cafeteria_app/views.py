from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from .cart import Cart
from .models import Product, Category, CategoryEvents, Events, Reserva
import qrcode
import io
import base64
from django.core.mail import EmailMessage

def events_view(request):
    categoriaevento=request.GET.get('categoriaevento')
    busqueda=request.GET.get('busqueda')
    eventsir=Events.objects.all()
    if categoriaevento:
        eventsir= eventsir.filter(CategoryEvents__name=categoriaevento)
    if busqueda:
        eventsir= eventsir.filter(name__icontains=busqueda)
    
    return render(request, 'cafeteria_app/events.html',{
        'eventsir': eventsir,
        'categoriesevents': CategoryEvents.objects.all()
    })
def event_detail(request, id):
    event = Events.objects.get(id=id)
    alimentos = list(event.alimentos.all())
    grupos = [alimentos[i:i+4] for i in range(0, len(alimentos), 4)]

    if request.method == 'POST':
        nombre_completo = request.POST.get('nombre_completo')
        correo = request.POST.get('gmail')
        num_asistentes = request.POST.get('num_asistentes')
        zona = request.POST.get('zona')
        evento_nombre = request.POST.get('evento_nombre')

        reserva = Reserva.objects.create(
            evento_nombre=evento_nombre,
            nombre_completo=nombre_completo,
            correo=correo,
            num_asistentes=num_asistentes,
            zona=zona,
        )

        # Generar QR
        qr_data = f"Reserva: {reserva.codigo} | Evento: {evento_nombre} | Nombre: {nombre_completo}"
        qr = qrcode.make(qr_data)
        buffer = io.BytesIO()
        qr.save(buffer, format='PNG')
        buffer.seek(0)
        qr_base64 = base64.b64encode(buffer.getvalue()).decode()

        # Enviar correo en segundo plano
        email = EmailMessage(
            subject=f'Reserva confirmada - {evento_nombre}',
            body=f'Hola {nombre_completo}, tu reserva está confirmada.\nPersonas: {num_asistentes}\nZona: {zona}',
            to=[correo],
        )
        buffer.seek(0)
        email.attach(f'qr_reserva.png', buffer.read(), 'image/png')
        import threading
        thread = threading.Thread(target=email.send)
        thread.start()

        return render(request, 'cafeteria_app/event_detail.html', {
            'event': event,
            'alimentos': alimentos,
            'grupos': grupos,
            'reserva': reserva,
            'qr_imagen': qr_base64,
            'confirmado': True,
        })

    return render(request, 'cafeteria_app/event_detail.html', {
        'event': event,
        'alimentos': alimentos,
        'grupos': grupos,
    })

def ejemplo(request):
    return render(request, 'cafeteria_app/ejemplo.html')

def home(request):
    products = Product.objects.all()
    return render(request, 'cafeteria_app/index.html', {'products': products})

def shop(request):
    products = Product.objects.all()
    return render(request, 'cafeteria_app/shop.html', {'products': products})

def menu(request):
    categories = request.GET.get('categoria')
    busqueda = request.GET.get('busqueda')
    productos = Product.objects.all()
    if categories:
        productos = productos.filter(category__name=categories)
    if busqueda:
        productos = productos.filter(name__icontains=busqueda)
    return render(request, 'cafeteria_app/menu.html', {'products': productos, 'categories': Category.objects.all()})

def gallery(request):
    return render(request, 'cafeteria_app/gallery.html')



def registro(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html', {
            'form': UserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                messages.success(request, 'Usuario registrado exitosamente')
                auth_login(request, user)
                return redirect('index')
                
            except:
                return render(request, 'registration/register.html', {
                    'form': UserCreationForm(),
                    'error': 'El nombre de usuario ya existe'
                })
        return render(request, 'registration/register.html', {
            'form': UserCreationForm(),
            'error': 'Contraseñas no coinciden'
        })

def signin(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'registration/login.html', {
                'error': 'Usuario o contraseña incorrectos.'
            })
        auth_login(request, user)
        return redirect('index')

def exit(request):
    logout(request)
    return redirect('index')

# carro de compras
@login_required
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cafeteria_app/cart.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product)
    return redirect('cart')


@login_required
def remove_from_cart_base(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product)
    return redirect(request.META.get('HTTP_REFERER', 'shop'))