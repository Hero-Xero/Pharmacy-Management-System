# admin_panel/admin.py
from django.contrib import admin
from PMS_Marketplace.models import Category, Product, User, Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


# ERROR: 
# <class 'PMS_Admin.models.ProductAdmin'>: (admin.E109) The value of 'list_display[1]' must not be a many-to-many field or a reverse foreign key.

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'price', 'stock')

