from django.shortcuts import render
from .models import AuthorProfile, Category, Tag, Post


def blog_page(request):
    posts = Post.objects.filter(is_draft=False)
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)

def blog_details(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'blog/single-blog.html', context)
