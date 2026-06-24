from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from .cart import Cart
from .models import Product, Category, CategoryEvents, Events,Pedido, PedidoItem
from django.views import View
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from core import settings
#---------------------------------------------------------------------------------
#Eventos gemnerales 
#---------------------------------------------------------------------------------
def events_view(request):
    categoria_nombre = request.GET.get('categoriaevento')
    busqueda = request.GET.get('busqueda')
    events = Events.objects.all()
    if categoria_nombre:
        events = events.filter(CategoryEvents__name=categoria_nombre)
    if busqueda:
        events = events.filter(name__icontains=busqueda)
    context = {
        'eventototal' : events,
        'cateventostotal' : CategoryEvents.objects.all(),
    }
    return render(request, 'cafeteria_app/events.html', context)


    
#Detalles de eventos, onda el template pss 
def event_detail(request, id):
    evento = get_object_or_404(Events, id=id)
    return render(request, 'cafeteria_app/event_detail.html', {
        'event': evento,
        'alimentos': evento.exclusive.all(),
        'imagenes': evento.imagenes.all()
    })

def ejemplo(request):
    return render(request, 'cafeteria_app/ejemplo.html')

def home(request):
    Product_all = Product.objects.all()
    #para los carruseles con ids dinamicas
    ##filtro de nuevos
    new = Product.objects.filter(is_new=True)
    group_new = [new[i: i + 4 ]for i in range (0, len(new), 4)]
    ##filtro de queridos
    best = Product.objects.filter(is_best=True)
    group_best = [best[i: i+ 4 ]for i in range (0, len(best),4)]
    context ={
        "products" : Product_all,
        "group_new" : group_new,
        "group_best" : group_best,
    }
    return render(request, 'cafeteria_app/index.html', context)

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
    product = get_object_or_404(Product, id=product_id) 
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity)
    return redirect('cart') 

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

@login_required
def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        return redirect('cart')
    if request.method == 'POST':
        retiro = request.POST.get('retiro', 'local')
        pedido = Pedido.objects.create(
            usuario=request.user,
            total=cart.get_total(),
            retiro=retiro
        )
        for item in cart:
            PedidoItem.objects.create(
                pedido=pedido,
                producto=item['product'],
                cantidad=item['quantity'],
                precio=item['price']
            )
        cart.clear()
        return render(request, 'cafeteria_app/finish.html', {'pedido': pedido})
    return render(request, 'cafeteria_app/checkout.html', {'cart': cart})

from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, id):
    producto = get_object_or_404(Product, id=id)
    return render(request, 'cafeteria_app/product_detail.html', {
        'product': producto
    })

class Send(View):
    def get(self, request, id):
        event = get_object_or_404(Events, id=id)
        return render(request, 'cafeteria_app/event_detail.html', {'event': event})

    def post(self, request, id):
        email = request.POST.get('email')
        event_name = request.POST.get('event_name')
        event = get_object_or_404(Events, id=id)
        event_name = event.name
        print(email)
        print(event_name)

        template = get_template('cafeteria_app/email_template.html')
        
        context = {
        'email': email,
        'event_name': event_name
    }
        content = template.render(context)
        msg = EmailMultiAlternatives(
            'correo de prueba',
            'Este es un correo de prueba',
            settings.EMAIL_HOST_USER,
            [email])
        
        msg.attach_alternative(content, 'text/html')
        msg.send()
        
        messages.success(request, 'Correo enviado correctamente')
        
        return redirect(request.META.get('HTTP_REFERER', '/'))