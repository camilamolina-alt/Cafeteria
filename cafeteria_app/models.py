from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.PositiveSmallIntegerField() #por ahora solo por ver que ondis
    details = models.TextField(blank = True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    def __str__(self):
        return self.name
    