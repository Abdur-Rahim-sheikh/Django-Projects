from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "this really does works"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gte=0)
        return data


class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review  # html will get data as lowercase of model_name (review)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        loaded_review = self.object
        request = self.request
        # favourite_id = request.session["favourite_review"]
        favourite_id = request.session.get("favourite_review")
        print(loaded_review.id,favourite_id)
        context["is_favourite"] = (int(favourite_id)==loaded_review.id)
        return context
    

class AddFavouriteView(View):
    def post(self,request):
        review_id = request.POST['review_id']

        request.session['favourite_review']=review_id

        return HttpResponseRedirect("/reviews/"+review_id)