from django.urls import path
from .views import agregar_producto , listar_producto, modificar_producto, panel_admin, products, eliminar_producto, listar_categoria, modificar_categoria,eliminar_categoria, agregar_categoria
from .views import events, agregar_evento, listar_evento, modificar_evento, eliminar_evento

urlpatterns = [

    path('', panel_admin, name='panel_admin'),
    ###urls para productos 
    path('products', products, name='products'),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('listar-producto/', listar_producto, name="listar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    #Urls para categorias de productos
    path('categorias/agregar/', agregar_categoria, name='agregar_categoria'),
    path('categorias/listar/', listar_categoria, name='listar_categoria'),
    path('categorias/modificar/<id>/', modificar_categoria, name='modificar_categoria'),
    path('categorias/eliminar/<id>/', eliminar_categoria, name='eliminar_categoria'),

    #URLS PARA EVENTOS
    path('events', events, name='events'),
    path('eventos/agregar/', agregar_evento, name='agregar_evento'),
    path('eventos/listar/', listar_evento, name='listar_evento'),
    path('eventos/modificar/<id>/', modificar_evento, name='modificar_evento'),
    path('eventos/eliminar/<id>/', eliminar_evento, name='eliminar_evento'),
]