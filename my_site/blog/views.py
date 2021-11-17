from typing import List
from django.shortcuts import render,get_object_or_404
from datetime import date
from django.http import HttpResponseRedirect
from .models import Post
from django.views.generic import ListView
from django.views import View
from .forms import CommentForm
from django.urls import reverse
# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3] #-for descending
    
#     return render(request,"blog/index.html",{
#         "posts":latest_posts
#     })
class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"
# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request,"blog/all-posts.html",{
#         "all_posts": all_posts
#     })

class PostDetailView(View):

    def is_stored_post(self,request,post_id):
        stored_posts = request.session.get("stored_posts")
        is_saved_for_later = False
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts

        return is_saved_for_later
        
    def get(self, request,slug):
        post = Post.objects.get(slug=slug)
       

        context = {
            "post": post,
            "post_tags":post.tags.all(),
            "comments": post.comments.all().order_by("-id"),
            "comment_form":CommentForm(),
            "saved_for_later": self.is_stored_post(request,post.id)
        }
        return render(request,"blog/post-details.html",context)

    def post(self,request,slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug = slug)
        if comment_form.is_valid():

            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))
        
        

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comments":post.comments.all().order_by("-id"),
            "comment_form":comment_form,
            "saved_for_later": self.is_stored_post(request,post.id)

        }
        return render(request,"blog/post-details.html",context)




# def post_detail(request,slug):
#     # all_posts = Post.objects.all().order_by("-date")
#     # specified_post = next(post for post in all_posts if post.slug==slug)
#     specified_post = get_object_or_404(Post,slug=slug)
#     return render(request,"blog/post-details.html",{
#         "post":specified_post,
#         "post_tags":specified_post.tags.all()
#     })


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}
        if stored_posts is None or len(stored_posts)==0:
            context["posts"]= []
            context["has_posts"]=False

        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"]=True

        return render(request, "blog/stored-posts.html",context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []
        post_id = int(request.POST["post_id"])

        # print(stored_posts,"agu")

        if post_id  not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
            
        request.session["stored_posts"]=stored_posts

        return HttpResponseRedirect("/")
