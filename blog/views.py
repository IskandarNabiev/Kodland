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

def post_create_view(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, "blog/posts.html", context)