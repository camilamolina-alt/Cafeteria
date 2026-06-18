from django.shortcuts import render
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

    contexto = {
        'total_productos': Product.objects.count(),
        'total_categorias': Category.objects.count(),
        'total_pedidos': Pedido.objects.count(),
        'total_eventos': Events.objects.count(),
        'top_productos': top_productos,
    }
    return render(request, 'panel_admin/panel_admin.html', contexto)

def products(request):
    products = Product.objects.all()
    return render(request, 'panel_admin/products.html')



