from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.house_list, name='house_list'),
    path('house/<int:house_id>/', views.house_detail, name='house_detail'),
    path('house/<int:house_id>/book/', views.book_house, name='book_house'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='booking/login.html'), name='login'),
]
