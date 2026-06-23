from django.urls import path
from .views import agregar_producto , listar_producto, modificar_producto, panel_admin, products, eliminar_producto


urlpatterns = [

    path('', panel_admin, name='panel_admin'),
    path('products', products, name='products'),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('listar-producto/', listar_producto, name="listar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    #path('eventos', views.eventos, name='eventos'),
    #path('promociones', views.promocion, name='promociones'),
]