from django.db import models
from django.contrib.auth.models import User
import uuid

# el uuid es para poder crear identificadores unicos universales para la reserva, por si acaso
# Create your models here.

#---------------------------------------------------------------------------------
#cOMIDA
#---------------------------------------------------------------------------------
class Category(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    descuento = models.IntegerField(default=0, verbose_name="Descuento")
    details = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock disponible")

    is_new = models.BooleanField(default=False, verbose_name="menu nuevo")
    is_best = models.BooleanField(default=False, verbose_name="mas queridos")
    def __str__(self):
        return self.name
    @property
    def precio_final(self):
        if self.descuento > 0:
            nuevo_precio = self.price * (1 - self.descuento / 100)
            return int(nuevo_precio)
        return self.price
    
class ImagenProducto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='imagenes')
    imageProduct = models.ImageField(upload_to='galeria_producto/')
    descripcion = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return f"Galeria: {self.product.name}"

#---------------------------------------------------------------------------------
#EVENTOS

#---------------------------------------------------------------------------------
class CategoryEvents(models.Model):
    name=models.CharField(max_length=15)
    def __str__(self):
        return self.name
    
class Events(models.Model):
    CategoryEvents = models.ForeignKey(CategoryEvents, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    fecha_inicio = models.DateTimeField(verbose_name="Inicio del evento", null=True, blank=True)
    fecha_fin = models.DateTimeField(verbose_name="Fin del evento", null=True, blank=True)

    def __str__(self):
        return self.name

    def ya_paso(self):
        from django.utils import timezone
        if self.fecha_fin is None:
            return False
        return timezone.now() > self.fecha_fin


class ExclusiveFood(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='exclusive')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.PositiveIntegerField() 
    image = models.ImageField(upload_to='alimentos/', blank=True, null=True)
    def __str__(self):
        return f"{self.nombre} ($ {self.precio})"

class ImagenEvento(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='eventos_galeria/')
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Galeria: {self.event.name}"

#---------------------------------------------------------------------------------

class Promotion(models.Model):
    name = models.CharField(max_length=100)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    target_food = models.OneToOneField(ExclusiveFood, on_delete=models.CASCADE)
#---------------------------------------------------------------------------------

#Carro

#---------------------------------------------------------------------------------
class CarritoItem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def subtotal(self):
        return self.producto.price * self.cantidad

    def __str__(self):
        return f"{self.usuario} - {self.producto.name}"
    
class Pedido(models.Model):
    RETIRO_CHOICES = [
        ('local', 'Retirar en local'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    retiro = models.CharField(max_length=20, choices=RETIRO_CHOICES, default='local')

    def __str__(self):
        return f"Pedido #{self.id} - {self.fecha.strftime('%d/%m/%Y')}"

class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.precio * self.cantidad

    def __str__(self):
        return f"{self.producto.name} x{self.cantidad}"
    
#---------------------------------------------------------------------------------

#LOS BANNERS
class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    texto_boton = models.CharField(max_length=30, blank=True, verbose_name="Texto del botón")
    link = models.CharField(max_length=200, blank=True, verbose_name="Enlace del botón")
    orden = models.PositiveIntegerField(default=0, verbose_name="Orden de aparición")

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return f"Banner #{self.id}"