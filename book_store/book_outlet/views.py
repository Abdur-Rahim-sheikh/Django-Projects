from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import Book
from django.db.models import Avg
# Create your views here.

def index(request):
    # -field_name means, order by the field 
    # but in descending order
    books = Book.objects.all().order_by("-title") 
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request,"book_outlet/index.html",{
        "books":books,
        "total_number_of_books":num_books,
        "average_rating":avg_rating
    })


def book_detail(request,slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book,slug=slug)
    return render(request,"book_outlet/book_detail.html",{
        "title":book.title,
        "author":book.author,
        "rating":book.rating,
        "is_bestsetller":book.is_bestselling
    })