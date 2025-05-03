
from django.shortcuts import render, redirect
from django.http import Http404
from PMS_Marketplace.models import Category, Product, Cart, CartItem, Order
from PMS_Accounts.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, "home.html")


# View to handle product category page
def category(request, name):
    formatted_name = name.replace("_", " ").lower()
    search_query = request.GET.get('q', '')

    if formatted_name == "all":
        products = Product.objects.all()
        if search_query:
            products = products.filter(
                Q(name__icontains=search_query) | Q(description__icontains=search_query)
            )
        return render(request, "category.html", {
            "category_name": "All Categories",
            "products": products
        })

    try:
        category = Category.objects.get(name=formatted_name)
    except Category.DoesNotExist:
        raise Http404("Category not found")

    products = Product.objects.filter(category=category)

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        )

    return render(request, "category.html", {
        "category_name": category.name.title(),
        "products": products
    })


# View to handle updating the cart item quantity
@login_required
def update_cart_item(request, cart_item_id):
    if request.method == 'POST':
        cart_item = CartItem.objects.get(id=cart_item_id)
        quantity = int(request.POST.get('quantity'))

        if quantity <= 0:
            cart_item.delete()  # Remove item if quantity is zero or less
        else:
            cart_item.quantity = quantity
            cart_item.save()

        return redirect(reverse('marketplace:cart'))


@login_required
def add_item_to_cart(request, product_id):
    if request.method == "POST":
        product = Product.objects.get(id=product_id)

        # Get or create a cart for the user
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Check if item already exists in the cart
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
        )
        if not created:
            cart_item.quantity += 1  # Increment if exists
        cart_item.save()

        return redirect('marketplace:category', name=request.POST.get("category_name").replace(" ", "_"))


# View to handle the cart page
@login_required
def cart(request):
    cart = Cart.objects.filter(user=request.user).first()

    if not cart:
        cart_items = []
        subtotal = 0
    else:
        cart_items = CartItem.objects.filter(cart=cart)

        # Add calculated total_price to each item
        for item in cart_items:
            item.total_price = round(item.product.price * item.quantity, 2)

        # Calculate subtotal from item.total_price
        subtotal = sum(item.total_price for item in cart_items)

    shipping_cost = 50
    total = subtotal + shipping_cost

    return render(request, "cart.html", {
        'cart_items': cart_items,
        'subtotal': round(subtotal, 2),
        'shipping': shipping_cost,
        'total': round(total, 2)
    })


# View to handle proceeding to checkout
@login_required
def checkout(request):
    cart = Cart.objects.filter(user=request.user).first()

    if not cart:
        return redirect('cart')  # No cart found, redirect to cart page

    cart_items = CartItem.objects.filter(cart=cart)
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    shipping_cost = 50  # Example shipping cost
    total = subtotal + shipping_cost

    # Create the order
    order = Order.objects.create(
        user=request.user,
        cart=cart,
        total_price=total,
        status='pending'
    )

    # Optionally, clear the cart after checkout
    cart_items.delete()

    # You can redirect to an order confirmation page
    return render(request, "order_confirmation.html", {
        'order': order
    })
