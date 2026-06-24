from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('shop/', views.shop, name='shop'),
    path('menu/', views.menu, name='menu'),
    path('gallery/', views.gallery, name='gallery'),
    path('events/', views.events_view, name='events'),
    path('events/<int:id>/', views.event_detail, name='event_detail'),
    path('exit/', views.exit, name='exit'),
    path('ejemplo/', views.ejemplo, name='ejemplo'),
    path('login/', views.signin, name='login'),
    path('signup/', views.registro, name='signup'),
    path('signup/', views.registro, name='signup'),  
    path('cart/', views.cart_detail, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/remove/base/<int:product_id>/', views.remove_from_cart_base, name='remove_from_cart_base'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<int:id>/', views.product_detail, name='products_detail'),
    path('events/<int:id>/send/', views.Send.as_view(), name='send'),
]