from django.shortcuts import render
from datetime import date
from django.http import Http404
all_posts = [
    {
        "slug":"hike-in-the-mountains",
        "image":"mountain.jfif",
        "author":"Abir",
        "date": date(2021,7,21),
        "title":"Mountain Hiking",
        "excerpt":"""I never went to this place,
                        but i want to go there when i'll be able to do that.
                    """,
       "content":"""Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                        Aperiam quod qui officia tempora eos sunt nemo molestiae veniam voluptates velit,
                        omnis sint odit iure debitis error facilis quam itaque fugit.
                        Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                        Aperiam quod qui officia tempora eos sunt nemo molestiae veniam voluptates velit,
                        omnis sint odit iure debitis error facilis quam itaque fugit.
                    """
    },
    {
        "slug":"Cutting-tree-easy",
        "image":"wood.jpg",
        "author":"Abdur Rahim",
        "date": date(1521,7,21),
        "title":"Love for tree",
        "excerpt":"""I never went to this place,
                        but i want to go there when i'll be able to do that.
                    """,
       "content":"""Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                        Aperiam quod qui officia tempora eos sunt nemo molestiae veniam voluptates velit,
                        omnis sint odit iure debitis error facilis quam itaque fugit.
                        Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                        Aperiam quod qui officia tempora eos sunt nemo molestiae veniam voluptates velit,
                        omnis sint odit iure debitis error facilis quam itaque fugit.
                    """
    },

    {
        "slug":"Coding-With-passion",
        "image":"coding.png",
        "author":"Abuhanif",
        "date": date(2405,7,21),
        "title":"Persistent Coder",
        "excerpt":"""I never went to this place,
                        but i want to go there when i'll be able to do that.
                    """,
       "content":"""Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                        Aperiam quod qui officia tempora eos sunt nemo molestiae veniam voluptates velit,
                        omnis sint odit iure debitis error facilis quam itaque fugit.
                        Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                        Aperiam quod qui officia tempora eos sunt nemo molestiae veniam voluptates velit,
                        omnis sint odit iure debitis error facilis quam itaque fugit.
                    """
    }

]

def get_date(post):
    return post.get('date')
# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request,"blog/index.html",{
        "posts":latest_posts
    })

def posts(request):
    
    return render(request,"blog/all-posts.html",{
        "all_posts": all_posts
    })

def post_detail(request,slug):
    
    specified_post = next(post for post in all_posts if post['slug']==slug)
    return render(request,"blog/post-details.html",{
        "post":specified_post
    })

