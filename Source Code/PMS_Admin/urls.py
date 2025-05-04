from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path("", views.dashboard_view, name="home"),
    path("add_product/", views.add_product, name="add_product"),
    path("add_category/", views.add_category, name="add_category")
]
