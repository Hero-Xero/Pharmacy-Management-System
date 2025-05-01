# admins/views.py
from django.shortcuts import render, redirect
from .forms import ProductForm, CategoryForm
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin_user(user):
    return user.is_authenticated and user.is_staff  # ← CHANGED THIS LINE

@login_required
@user_passes_test(is_admin_user)
def index(request):
    return render(request, 'admin/index.html')

@login_required
@user_passes_test(is_admin_user)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Adjust this to your actual route
    else:
        form = ProductForm()
    return render(request, 'admin/add_product.html', {'form': form})
    

@login_required
@user_passes_test(is_admin_user)
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')  # Adjust this to your actual route
    else:
        form = CategoryForm()
    return render(request, 'admin/add_category.html', {'form': form})
