from django.db import models
from django.contrib.auth.models import User
import uuid

# el uuid es para poder crear identificadores unicos universales para la reserva, por si acaso
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField() 
    details = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    is_new = models.BooleanField(default=False, verbose_name="menu nuevo")
    is_best = models.BooleanField(default=False, verbose_name="mas queridos")

    def __str__(self):
        return self.name
    
class CarritoItem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def subtotal(self):
        return self.producto.price * self.cantidad

    def __str__(self):
        return f"{self.usuario} - {self.producto.name}"
    
class Reserva(models.Model):
    codigo = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    evento_nombre = models.CharField(max_length=200)
    nombre_completo = models.CharField(max_length=200)
    num_asistentes = models.IntegerField()
    zona = models.CharField(max_length=50)
    correo = models.EmailField()
    asistio = models.BooleanField(default=False)
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_completo} - {self.evento_nombre}"