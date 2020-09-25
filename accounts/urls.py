from django.urls import path
from . import views

urlpatterns = [
    path('',views.RegisterPage,name='register'),
    path('login',views.LoginPage,name='login'),
    path('home',views.home,name='home'),
    path('logout',views.LogoutPage,name='logout'),
    path('edit/<str:pk>',views.Edit,name='edit'),
    path('delete/<str:pk>',views.Delete,name='delete'),
    path('create',views.Create_Client,name='create_client'),
    path('bmi/<str:pk>',views.Bmi,name='bmi'),
    path('index',views.index,name='index')
    
]
