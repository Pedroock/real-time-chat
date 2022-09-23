from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomAuthForm

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', 
                                                authentication_form=CustomAuthForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
