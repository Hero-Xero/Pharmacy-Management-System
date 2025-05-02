from django.contrib.auth.decorators import login_required
from PMS_Accounts.decorators import admin_required
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ProductForm, CategoryForm
from PMS_Marketplace.models import Product, Category, Order
from PMS_Accounts.models import User
from django.db.models import Sum
from datetime import date


@login_required
@admin_required
def dashboard_view(request):
    total_customers = User.objects.filter(is_staff=False, is_superuser=False).count()
    total_medicines = Product.objects.count()
    out_of_stock = Product.objects.filter(stock=0).count()
    expired_medicines = Product.objects.filter(expiry_date__lt=date.today()).count()

    # Sales and purchase values could be real calculations if you store this info in Order model
    total_sales = Order.objects.filter(status='delivered').aggregate(total=Sum('total_price'))['total'] or 0
    total_purchase = 0  # Placeholder unless you have purchase data

    context = {
        "total_customers": total_customers,
        "total_medicines": total_medicines,
        "out_of_stock": out_of_stock,
        "expired_medicines": expired_medicines,
        "sales": total_sales,
        "purchase": total_purchase,
    }
    return render(request, "dashboard.html", context)

@login_required
@admin_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard:home'))  # <-- Updated
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

@login_required
@admin_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard:home'))  # <-- Updated
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})
