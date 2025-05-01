from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_client, name='register_client'),
    path('login/', views.login_client, name='login_client'),
    path('logout/', views.logout_client, name='logout_client'),
]
