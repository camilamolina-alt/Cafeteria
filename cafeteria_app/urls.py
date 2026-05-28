from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('shop/', views.shop, name='shop'),
    path('menu/', views.menu, name='menu'),
    path('gallery/', views.gallery, name='gallery'),
    path('events/', views.events, name='events'),
    path('cart/', views.cart, name='cart')
]
