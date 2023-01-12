# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('<int:id>', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('view/', views.view, name='view'),
    path('password-change/', views.ChangePasswordView.as_view(), name='password_change'),
]