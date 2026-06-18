from django.urls import path
from . import views


urlpatterns = [

    path('', views.panel_admin, name='panel_admin'),
    path('products', views.products, name='products'),
    #path('eventos', views.eventos, name='eventos'),
    #path('promociones', views.promocion, name='promociones'),
]