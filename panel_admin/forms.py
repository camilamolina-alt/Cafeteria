from django import forms
from cafeteria_app.models import Product, Category, Events
from django.contrib.auth.forms import UserCreationForm


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

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name' : 'Nombre de la categoria'
        }

##Aqui estan los forms de los eventos
class EventoForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['CategoryEvents', 'name', 'description', 'image', 'fecha_inicio', 'fecha_fin']
        labels = {
            'CategoryEvents': 'Categoría',
            'name': 'Nombre del evento',
            'description': 'Descripción',
            'image': 'Imagen',
            'fecha_inicio': 'Fecha y hora de inicio',
            'fecha_fin': 'Fecha y hora de fin',
        }
        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'fecha_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }

        