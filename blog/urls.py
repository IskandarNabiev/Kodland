from django.contrib import admin
from django.urls import path, include
from .views import home, post_create_view

urlpatterns = [
    path('', home, name='blog-home'),
    path('posts/', post_create_view, name='post_create')
]