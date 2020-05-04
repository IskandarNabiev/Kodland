from django.shortcuts import render
from django.views import View

from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

    

class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/posts.html', context={'form': form})
