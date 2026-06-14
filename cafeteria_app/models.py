from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#ARCHIVOS DEL PANEL DE ADMIN 
class Category(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.PositiveSmallIntegerField() #por ahora solo por ver que ondis
    details = models.TextField(blank = True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
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
    
