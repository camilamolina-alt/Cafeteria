from django.shortcuts import render, redirect, get_object_or_404
from panel_admin.forms import ProductoForm, CategoryForm, EventoForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Sum
from cafeteria_app.models import Category, Product, Events, Pedido

def es_admin(user):
    return user.is_staff

@login_required
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

def products(request):
    products = Product.objects.all()
    return render(request, 'panel_admin/productos/products.html', {'products': products})

def agregar_producto(request):
    data={
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
            return redirect(to="listar_producto")
        else:
            data["form"] = formulario

    return render (request,'panel_admin/productos/agregarProducto.html',data)

def listar_producto(request):
    productos = Product.objects.all()

    data = {
        'productos' : productos
    }
    return render (request,'panel_admin/productos/listarProducto.html', data)

def modificar_producto(request,id):
    producto = get_object_or_404(Product, id = id)
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_producto")
        else:
            data["form"] = formulario
    return render (request,'panel_admin/productos/modificarProducto.html',data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Product, id = id)
    producto.delete()
    return redirect(to="listar_producto")

###Para las categorias###
def agregar_categoria(request):
    data = {
        'form': CategoryForm()
    }

    if request.method == 'POST':
        formulario = CategoryForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
            return redirect(to="listar_categoria")
        else:
            data["form"] = formulario

    return render(request, 'panel_admin/productos/agregarCategoria.html', data)

def listar_categoria(request):
    categorias = Category.objects.all()

    data = {
        'categorias': categorias
    }
    return render(request, 'panel_admin/productos/listarCategoria.html', data)

def modificar_categoria(request, id):
    categoria = get_object_or_404(Category, id=id)
    data = {
        'form': CategoryForm(instance=categoria)
    }
    if request.method == 'POST':
        formulario = CategoryForm(data=request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_categoria")
        else:
            data["form"] = formulario
    return render(request, 'panel_admin/productos/modificarCategoria.html', data)

def eliminar_categoria(request, id):
    categoria = get_object_or_404(Category, id=id)
    categoria.delete()
    return redirect(to="listar_categoria")

##Inicio de vistas para eventos 
def event(request):
    eventos = Events.objects.all()
    return render(request, 'panel_admin/eventos/event.html', {'event': eventos})



def listar_evento(request):
    eventos = Events.objects.all()
    data = {'eventos': eventos}
    return render(request, 'panel_admin/eventos/listarEvento.html', data)

def agregar_evento(request):
    data = {'form': EventoForm()}
    if request.method == 'POST':
        formulario = EventoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_evento")
        else:
            data["form"] = formulario
    return render(request, 'panel_admin/eventos/agregarEvento.html', data)

def modificar_evento(request, id):
    evento = get_object_or_404(Events, id=id)
    data = {'form': EventoForm(instance=evento)}
    if request.method == 'POST':
        formulario = EventoForm(data=request.POST, instance=evento, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_evento")
        else:
            data["form"] = formulario
    return render(request, 'panel_admin/eventos/modificarEvento.html', data)

def eliminar_evento(request, id):
    evento = get_object_or_404(Events, id=id)
    evento.delete()
    return redirect(to="listar_evento")
