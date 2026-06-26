from django.conf import settings
from decimal import Decimal
from .models import Product

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.precio_final)
            }
        
        if override_quantity:
            nueva_cantidad = quantity
        else:
            nueva_cantidad = self.cart[product_id]['quantity'] + quantity
            
        if nueva_cantidad > product.stock:
            nueva_cantidad = product.stock
            
        if nueva_cantidad >= 0:
            self.cart[product_id]['quantity'] = nueva_cantidad
            self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            precio_actual = item['product'].precio_final
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        
        total = 0
        for product in products:
            product_id = str(product.id)
            if product_id in self.cart:
                quantity = self.cart[product_id]['quantity']
                total += product.precio_final * quantity
        return total

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()