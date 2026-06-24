from django.urls import path
from .views import agregar_producto , listar_producto, modificar_producto, panel_admin, products, eliminar_producto, listar_categoria, modificar_categoria,eliminar_categoria, agregar_categoria
from .views import events, agregar_evento, listar_evento, modificar_evento, eliminar_evento, login_admin
from .views import agregar_exclusivo,listar_exclusivo,modificar_exclusivo,eliminar_exclusivo, agregar_imagen_evento,modificar_imagen_evento,eliminar_imagen_evento,listar_imagen_evento
from .views import agregar_banner,listar_banner,modificar_banner,eliminar_banner

urlpatterns = [
    path('', panel_admin, name='admin_panel_admin'),
    path('login/', login_admin, name='login_admin'),
    ##URL PARA LOS BANNERS
    path('banners/agregar/', agregar_banner, name='admin_agregar_banner'),
    path('banners/listar/', listar_banner, name='admin_listar_banner'),
    path('banners/modificar/<id>/', modificar_banner, name='admin_modificar_banner'),
    path('banners/eliminar/<id>/', eliminar_banner, name='admin_eliminar_banner'),

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
# SIGUE SIENDO URLS PARA EVENTOS DEL ADMIN PERO ITEMS ESPECIALES####
    path('exclusivos/agregar/', agregar_exclusivo, name='admin_agregar_exclusivo'),
    path('exclusivos/listar/', listar_exclusivo, name='admin_listar_exclusivo'),
    path('exclusivos/modificar/<id>/', modificar_exclusivo, name='admin_modificar_exclusivo'),
    path('exclusivos/eliminar/<id>/', eliminar_exclusivo, name='admin_eliminar_exclusivo'),
# SIGUE SIENDO URLS PARA EVENTOS DEL ADMIN PERO ITEMS ESPECIALE Y AHORA IMAGENESS####
path('imagenes-evento/agregar/', agregar_imagen_evento, name='admin_agregar_imagen_evento'),
    path('imagenes-evento/listar/', listar_imagen_evento, name='admin_listar_imagen_evento'),
    path('imagenes-evento/modificar/<id>/', modificar_imagen_evento, name='admin_modificar_imagen_evento'),
    path('imagenes-evento/eliminar/<id>/', eliminar_imagen_evento, name='admin_eliminar_imagen_evento'),
]