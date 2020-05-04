from datetime import timezone
from django.shortcuts import render
from django.views import View

from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

def last(request):
    last_posts = Post.objects.filter(date_posted)[:1][::-1]
    context = {'last_posts': last_posts}
    return render(request, 'blog/home.html', context)

class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/posts.html', context={'form': form})
