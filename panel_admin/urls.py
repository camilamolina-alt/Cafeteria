from django.urls import path
from .views import agregar_producto , listar_producto, modificar_producto, panel_admin, products, eliminar_producto, listar_categoria, modificar_categoria,eliminar_categoria, agregar_categoria
from .views import events, agregar_evento, listar_evento, modificar_evento, eliminar_evento, login_admin

urlpatterns = [
    path('', panel_admin, name='admin_panel_admin'),
    path('login/', login_admin, name='login_admin'),
    ###urls para productos 
    path('products', products, name='products'),
    path('agregar-producto/', agregar_producto, name="admin_agregar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="admin_modificar_producto"),
    path('listar-producto/', listar_producto, name="admin_listar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="admin_eliminar_producto"),
    #Urls para categorias de productos
    path('categorias/agregar/', agregar_categoria, name='admin_agregar_categoria'),
    path('categorias/listar/', listar_categoria, name='admin_listar_categoria'),
    path('categorias/modificar/<id>/', modificar_categoria, name='admin_modificar_categoria'),
    path('categorias/eliminar/<id>/', eliminar_categoria, name='admin_eliminar_categoria'),

# URLS PARA EVENTOS DEL ADMIN
    path('events/', events, name='admin_events'),
    path('eventos/agregar/', agregar_evento, name='admin_agregar_evento'),
    path('eventos/listar/', listar_evento, name='admin_listar_evento'),
    path('eventos/modificar/<id>/', modificar_evento, name='admin_modificar_evento'),
    path('eventos/eliminar/<id>/', eliminar_evento, name='admin_eliminar_evento'),
]