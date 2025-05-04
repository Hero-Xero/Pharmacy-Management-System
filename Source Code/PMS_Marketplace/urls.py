from django.urls import path
from . import views

app_name = "marketplace"
urlpatterns = [
    path("", views.index, name="home"),
    path("cart/", views.cart, name="cart"),
    path("category/<str:name>", views.category, name="category"),
    path("checkout/", views.checkout, name="checkout"),
    path("update_cart_item/<int:cart_item_id>/", views.update_cart_item, name="update_cart_item"),
    path("add_to_cart/<int:product_id>/", views.add_item_to_cart, name="add_item"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
