from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
# Create your views here.
class ReviewView(View):
    def get(self,request):
        form = ReviewForm()
        return render(request,"reviews/review.html",{
            "form":form
        })
    
    def post(self,request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request,"reviews/review.html",{
        "form":form
    })

# class ThankYouView(View):

#     def get(self,request):
#         return render(request,"reviews/thank_you.html")

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] ="this really does works"
        return context

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gte = 4)
        return data
    
class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review   #html will get data as lowercase of model_name (review)

