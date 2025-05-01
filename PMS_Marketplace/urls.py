from django.urls import path
from . import views

# app_name = "marketplace"
urlpatterns = [
    path("", views.index, name="index"),
    path("cart/", views.cart, name="cart"),
    path("category/<str:name>", views.category, name="category"),
]
