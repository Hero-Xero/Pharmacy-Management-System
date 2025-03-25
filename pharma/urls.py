from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('register', views.client_register, name='register'),
    path('login', views.login_view, name='login'),
    path('users', views.users, name='users'),
    path('category/<str:category_name>', views.category, name='category'),
]
