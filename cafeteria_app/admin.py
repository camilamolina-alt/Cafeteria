from django.contrib import admin
from .models import Category, Product, CategoryEvents, Events, AlimentoEvento

admin.site.register(Category)
admin.site.register(Product)
#eventos
admin.site.register(CategoryEvents)
admin.site.register(Events)
admin.site.register(AlimentoEvento)