from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from user_manager.views.auth_view import UserLoginView, UserRegisterView
from user_manager.views.web_view import home_view, contact_view
from user_manager.views.render_view import render_project
from user_manager.views.error_view import custom_404_view
from user_manager.views.dashboard_views import dashboard_view, logout_view
urlpatterns = [
    path('', render_project, name='home'),
    path('contact/', contact_view, name='contact'),
    path('login/', UserLoginView.as_view(), name='account_login'),
    path('register/', UserRegisterView.as_view(), name='account_register'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), name='account_password_reset'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
]

handler404 = custom_404_view
