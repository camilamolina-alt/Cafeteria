from django.contrib import admin
from .models import Category, Product


admin.site.register(Category)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'details', 'category', 'price', 'is_new', 'is_best')
    list_filter = ('is_new', 'is_best', 'category')
    search_fields = ('name',)
    list_editable = ('is_new', 'is_best')