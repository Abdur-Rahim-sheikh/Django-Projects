from django.shortcuts import render,get_object_or_404
from datetime import date
from django.http import Http404
from .models import Post


def get_date(post):
    return post.get('date')
# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3] #-for descending
    
    return render(request,"blog/index.html",{
        "posts":latest_posts
    })

def posts(request):
    all_posts = Post.objects.all()
    return render(request,"blog/all-posts.html",{
        "all_posts": all_posts
    })

def post_detail(request,slug):
    # all_posts = Post.objects.all().order_by("-date")
    # specified_post = next(post for post in all_posts if post.slug==slug)
    specified_post = get_object_or_404(Post,slug=slug)
    return render(request,"blog/post-details.html",{
        "post":specified_post,
        "post_tags":specified_post.tags.all()
    })

