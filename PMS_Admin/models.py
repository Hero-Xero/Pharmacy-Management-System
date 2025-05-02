# admin_panel/admin.py
from django.contrib import admin
from marketplace.models import Category, Product, User, Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')

# You can similarly register User and Order if needed
