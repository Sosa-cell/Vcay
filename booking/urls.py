from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.house_list, name='house_list'),
    path('house/<int:house_id>/', views.house_detail, name='house_detail'),
    path('house/<int:house_id>/book/', views.book_house, name='book_house'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='booking/login.html'), name='login'),
    # Password reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='booking/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='booking/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='booking/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='booking/password_reset_complete.html'), name='password_reset_complete'),
]
