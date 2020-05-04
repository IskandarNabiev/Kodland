from django.contrib import admin
from django.urls import path, include
from .views import home, PostCreate

urlpatterns = [
    path('', home, name='blog-home'),
    path('posts/', PostCreate.as_view(), name='post_create')
]