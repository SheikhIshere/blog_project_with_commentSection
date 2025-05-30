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
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('add/', views.add_post, name= 'add_post'),
    path('add/', views.AddPostCreateView.as_view(), name= 'add_post'),
    # path('edit/<int:id>', views.edit_post, name= 'edit_post'),
    path('edit/<int:id>', views.EditPostView.as_view(), name= 'edit_post'), 
    # path('delete/<int:id>', views.delet_post, name= 'delete_post'),
    path('delete/<int:id>', views.ModelDeleteView.as_view(), name= 'delete_post'),
    # path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/<int:id>/', views.ModelDetailView.as_view(), name='post_detail'),

    # for like at the post
     path('like/<int:post_id>/', views.like_post, name='like_post'),
] 