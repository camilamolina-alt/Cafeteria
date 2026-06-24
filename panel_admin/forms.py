from django import forms
from cafeteria_app.models import Product, Category, Events, ExclusiveFood, ImagenEvento,Banner
from django.contrib.auth.forms import UserCreationForm


class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['image', 'texto_boton', 'link', 'orden']
        labels = {
            'image': 'Imagen',
            'texto_boton': 'Texto del botón',
            'link': 'Enlace',
            'orden': 'Orden de aparición',
        }


class ProductoForm(forms.ModelForm):
    
    descuento = forms.IntegerField(
        label = 'Descuento',
        required=False,
        min_value=0,
        max_value=100,
        initial=0,
        help_text='ingresar un valor de 0 a 100, dejar en 0 si no hay descuento'
    )
    
    class Meta:
        model = Product
<<<<<<< HEAD
        fields = ['category', 'name', 'price', 'descuento', 'details', 'image', 'is_new', 'is_best']
        labels = {
            'category': 'Categoría',
            'name': 'Nombre del producto',
            'price': 'Precio Original',
            'descuento': 'Descuento',
=======
        fields = ['category', 'name', 'price', 'stock', 'details', 'image', 'is_new', 'is_best']
        labels = {
            'category': 'Categoría',
            'name': 'Nombre del producto',
            'price': 'Precio',
            'stock': 'Stock disponible',
>>>>>>> 91f3e00900938ce7f2cbb4062ab7efcae7b14353
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

class ExclusiveFoodForm(forms.ModelForm):
    class Meta:
        model = ExclusiveFood
        fields = ['event', 'nombre', 'descripcion', 'precio', 'image']
        labels = {
            'event': 'Evento',
            'nombre': 'Nombre del producto exclusivo',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'image': 'Imagen',
        }

class ImagenEventoForm(forms.ModelForm):
    class Meta:
        model = ImagenEvento
        fields = ['event', 'imagen', 'descripcion']
        labels = {
            'event': 'Evento',
            'imagen': 'Imagen',
            'descripcion': 'Descripción',
        }