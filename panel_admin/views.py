from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from panel_admin.forms import ProductoForm, CategoryForm, EventoForm, ExclusiveFoodForm, ImagenEventoForm, BannerForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Sum
from cafeteria_app.models import Category, Product, Events, Pedido, ExclusiveFood, ImagenEvento, Banner

def es_admin(user):
    return user.is_staff

def login_admin(request):
    if request.method == 'GET':
        return render(request, 'panel_admin/register/login_admin.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'panel_admin/register/login_admin.html', {
                'error': 'Usuario o contraseña incorrectos.'
            })
        if not user.is_staff:
            return render(request, 'panel_admin/register/login_admin.html', {
                'error': 'No tienes permisos de administrador.'
            })
        auth_login(request, user)
        return redirect('admin_panel_admin')

@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def panel_admin(request):
    top_productos = Product.objects.annotate(
        total_vendido=Sum('pedidoitem__cantidad')
    ).order_by('-total_vendido')[:5]

    data = {
        'total_productos': Product.objects.count(),
        'total_categorias': Category.objects.count(),
        'total_pedidos': Pedido.objects.count(),
        'total_eventos': Events.objects.count(),
        'top_productos': top_productos,
    }
    return render(request, 'panel_admin/panel_admin.html', data)


@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def products(request):
    products = Product.objects.all()
    return render(request, 'panel_admin/productos/products.html', {'products': products})


@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def agregar_producto(request):
    data={
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
            return redirect(to="admin_listar_producto")
        else:
            data["form"] = formulario

    return render (request,'panel_admin/productos/agregarProducto.html',data)


@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def listar_producto(request):
    productos = Product.objects.all()

    data = {
        'productos' : productos
    }
    return render (request,'panel_admin/productos/listarProducto.html', data)


@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def modificar_producto(request,id):
    producto = get_object_or_404(Product, id = id)
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'modificado correctamente')
            return redirect(to="admin_listar_producto")
        else:
            data["form"] = formulario
    return render (request,'panel_admin/productos/modificarProducto.html',data)



@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def eliminar_producto(request, id):
    producto = get_object_or_404(Product, id = id)
    producto.delete()
    messages.success(request, 'eliminado correctamente')
    return redirect(to="admin_listar_producto")

###Para las categorias###



@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def agregar_categoria(request):
    data = {
        'form': CategoryForm()
    }

    if request.method == 'POST':
        formulario = CategoryForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
            return redirect(to="admin_listar_categoria")
        else:
            data["form"] = formulario

    return render(request, 'panel_admin/productos/agregarCategoria.html', data)


@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def listar_categoria(request):
    categorias = Category.objects.all()

    data = {
        'categorias': categorias
    }
    return render(request, 'panel_admin/productos/listarCategoria.html', data)


@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def modificar_categoria(request, id):
    categoria = get_object_or_404(Category, id=id)
    data = {
        'form': CategoryForm(instance=categoria)
    }
    if request.method == 'POST':
        formulario = CategoryForm(data=request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="admin_listar_categoria")
        else:
            data["form"] = formulario
    return render(request, 'panel_admin/productos/modificarCategoria.html', data)



@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Category, id=id)
    categoria.delete()
    messages.success(request, 'eliminado correctamente')
    return redirect(to="admin_listar_categoria")

##Inicio de vistas para eventos 

@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def events(request):
    eventos = Events.objects.all()
    return render(request, 'panel_admin/eventos/event.html', {'event': eventos})


@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def listar_evento(request):
    eventos = Events.objects.all()
    data = {'eventos': eventos}
    return render(request, 'panel_admin/eventos/listarEvento.html', data)



@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def agregar_evento(request):
    data = {'form': EventoForm()}
    if request.method == 'POST':
        formulario = EventoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="admin_listar_evento")
        else:
            data["form"] = formulario
    return render(request, 'panel_admin/eventos/agregarEvento.html', data)



@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def modificar_evento(request, id):
    evento = get_object_or_404(Events, id=id)
    data = {'form': EventoForm(instance=evento)}
    if request.method == 'POST':
        formulario = EventoForm(data=request.POST, instance=evento, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="admin_listar_evento")
        else:
            data["form"] = formulario
    return render(request, 'panel_admin/eventos/modificarEvento.html', data)


@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def eliminar_evento(request, id):
    evento = get_object_or_404(Events, id=id)
    evento.delete()
    messages.success(request, 'eliminado correctamente')
    return redirect(to="admin_listar_evento")

##exclusivo del evento###


@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def listar_exclusivo(request):
    exclusivos = ExclusiveFood.objects.all()
    data = {'exclusivos': exclusivos}
    return render(request, 'panel_admin/eventos/listarExclusivo.html', data)


@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def agregar_exclusivo(request):
    data = {'form': ExclusiveFoodForm()}
    if request.method == 'POST':
        formulario = ExclusiveFoodForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="admin_listar_exclusivo")
        else:
            data["form"] = formulario
    return render(request, 'panel_admin/eventos/agregarExclusivo.html', data)



@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def modificar_exclusivo(request, id):
    exclusivo = get_object_or_404(ExclusiveFood, id=id)
    data = {'form': ExclusiveFoodForm(instance=exclusivo)}
    if request.method == 'POST':
        formulario = ExclusiveFoodForm(data=request.POST, instance=exclusivo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="admin_listar_exclusivo")
        else:
            data["form"] = formulario
    return render(request, 'panel_admin/eventos/modificarExclusivo.html', data)



@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def eliminar_exclusivo(request, id):
    exclusivo = get_object_or_404(ExclusiveFood, id=id)
    exclusivo.delete()
    messages.success(request, 'eliminado correctamente')
    return redirect(to="admin_listar_exclusivo")



@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def listar_imagen_evento(request):
    imagenes = ImagenEvento.objects.all()
    data = {'imagenes': imagenes}
    return render(request, 'panel_admin/eventos/listarImagenEvento.html', data)



@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def agregar_imagen_evento(request):
    data = {'form': ImagenEventoForm()}
    if request.method == 'POST':
        formulario = ImagenEventoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="admin_listar_imagen_evento")
        else:
            data["form"] = formulario
    return render(request, 'panel_admin/eventos/agregarImagenEvento.html', data)



@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def modificar_imagen_evento(request, id):
    imagen = get_object_or_404(ImagenEvento, id=id)
    data = {'form': ImagenEventoForm(instance=imagen)}
    if request.method == 'POST':
        formulario = ImagenEventoForm(data=request.POST, instance=imagen, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="admin_listar_imagen_evento")
        else:
            data["form"] = formulario
    return render(request, 'panel_admin/eventos/modificarImagenEvento.html', data)



@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def eliminar_imagen_evento(request, id):
    imagen = get_object_or_404(ImagenEvento, id=id)
    imagen.delete()
    messages.success(request, 'eliminado correctamente')
    return redirect(to="admin_listar_imagen_evento")

##BANNER


@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def listar_banner(request):
    banners = Banner.objects.all()
    data = {'banners': banners}
    return render(request, 'panel_admin/banners/listarBanner.html', data)



@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def agregar_banner(request):
    data = {'form': BannerForm()}
    if request.method == 'POST':
        formulario = BannerForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="admin_listar_banner")
        else:
            data["form"] = formulario
    return render(request, 'panel_admin/banners/agregarBanner.html', data)


@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def modificar_banner(request, id):
    banner = get_object_or_404(Banner, id=id)
    data = {'form': BannerForm(instance=banner)}
    if request.method == 'POST':
        formulario = BannerForm(data=request.POST, instance=banner, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="admin_listar_banner")
        else:
            data["form"] = formulario
    return render(request, 'panel_admin/banners/modificarBanner.html', data)



@login_required(login_url='login_admin')
@user_passes_test(es_admin)
def eliminar_banner(request, id):
    banner = get_object_or_404(Banner, id=id)
    banner.delete()
    messages.success(request, 'eliminado correctamente')
    return redirect(to="admin_listar_banner")