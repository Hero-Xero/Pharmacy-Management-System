from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "home.html")

def cart(request):
    return render(request, "cart.html")

def category(request, name):
    name = name.replace("_", " ").title()
    return render(request, "category.html", {
        "category_name": name
    })