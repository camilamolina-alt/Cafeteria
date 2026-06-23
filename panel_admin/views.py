from django.shortcuts import render, redirect, get_object_or_404
from cafeteria_app.forms import ProductoForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Sum
from cafeteria_app.models import Category, Product, Events, Pedido, PedidoItem
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

