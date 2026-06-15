from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from .cart import Cart
from .models import Product, Category
#-----------------------------------


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


#Solo ando probando
def events(request):
    if request.method == 'POST':
        reserva = Reserva.objects.create(
            evento_nombre=request.POST.get('evento_nombre'),
            nombre_completo=request.POST.get('nombre_completo'),
            num_asistentes=request.POST.get('num_asistentes'),
            zona=request.POST.get('zona'),
            correo=request.POST.get('gmail'),  # corregido
        )

        # Generar QR
        qr = qrcode.make(str(reserva.codigo))
        buffer = io.BytesIO()
        qr.save(buffer, format='PNG')
        buffer.seek(0)
        qr_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        # Enviar por correo
        email = EmailMessage(
            subject=f'Reserva confirmada - {reserva.evento_nombre}',
            body=f'Hola {reserva.nombre_completo},\n\nTu reserva para "{reserva.evento_nombre}" está confirmada.\nPresenta el QR adjunto al llegar al local.\n\nNos vemos pronto!',
            to=[reserva.correo],
        )
        email.attach('qr_reserva.png', buffer.getvalue(), 'image/png')
        email.send()

        return render(request, 'cafeteria_app/events.html', {
            'reserva_exitosa': True,
            'qr_imagen': qr_base64,
            'reserva': reserva,
        })

    return render(request, 'cafeteria_app/events.html')

#-------------------------------------------------------------
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