"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
# from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', views.register, name= 'register'),
    # path('login/', views.user_login, name= 'user_login'),
    path('login/', views.UserLoginView.as_view(), name= 'user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    # path('logout/', views.ProductionLogoutView.as_view(), name='user_logout'), 
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/', views.profile, name= 'profile'),
    path('profile/pass_change/', views.pass_change, name= 'pass_change'),
]
