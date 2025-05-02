from django.shortcuts import render
from PMS_Marketplace.models import Category, Product
from django.http import Http404


# Create your views here.
def index(request):
    return render(request, "home.html")

def cart(request):
    return render(request, "cart.html")

def category(request, name):
    formatted_name = name.replace("_", " ").lower()

    try:
        category = Category.objects.get(name=formatted_name)
    except Category.DoesNotExist:
        raise Http404("Category not found")

    products = Product.objects.filter(category=category)

    return render(request, "category.html", {
        "category_name": category.name.title(),
        "products": products
    })