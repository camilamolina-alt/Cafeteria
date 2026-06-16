from django.contrib import admin
from .models import Category, Product, CategoryEvents, Events, AlimentoEvento, ImagenEvento

admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'details', 'category', 'price', 'is_new', 'is_best')
    list_filter = ('is_new', 'is_best', 'category')
    search_fields = ('name',)
    list_editable = ('is_new', 'is_best')

@admin.register(CategoryEvents)
class CategoryEventsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('name', 'CategoryEvents')
    list_filter = ('CategoryEvents',)
    search_fields = ('name',)

@admin.register(AlimentoEvento)
class AlimentoEventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'event', 'es_promocion')
    list_filter = ('es_promocion', 'event')
    search_fields = ('nombre',)
    list_editable = ('es_promocion',)

@admin.register(ImagenEvento)
class ImagenEventoAdmin(admin.ModelAdmin):
    list_display = ('event', 'descripcion')
    list_filter = ('event',)