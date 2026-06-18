from django import forms
from .models import Product, Category
from django.contrib.auth.forms import UserCreationForm

class customUserCreationForm(UserCreationForm):
    pass

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'details', 'image', 'is_new', 'is_best']
        labels = {
            'category': 'Categoría',
            'name': 'Nombre del producto',
            'price': 'Precio',
            'details': 'Descripción',
            'image': 'Imagen',
            'is_new': 'Nuedvo ingreso',
            'is_best': 'Recomendados',
        }
