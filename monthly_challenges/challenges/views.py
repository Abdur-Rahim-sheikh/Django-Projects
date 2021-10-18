from django.shortcuts import render

# Create your views here.
from django.http import (Http404,
                        HttpResponseNotFound,
                        HttpResponseRedirect)
from django.urls import reverse

# from django.template.loader import render_to_string
monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february":"Walk for atleast 20 minutes every day",
    "march":"Learn Django for at least 20 minutes every day",
    "april": "Eat no meat for the entire month!",
    "may":"Walk for atleast 20 minutes every day",
    "june":"Learn Django for at least 20 minutes every day",
    "july": "Eat no meat for the entire month!",
    "august":"Walk for atleast 20 minutes every day",
    "september":"Learn Django for at least 20 minutes every day",
    "october": "Eat no meat for the entire month!",
    "november":"Walk for atleast 20 minutes every day",
    # "december":"Learn Django for at least 20 minutes every day"
    "december":None
}

def monthly_challenges_by_number(reqeust,month):
    months = list(monthly_challenges.keys())
    if(month> len(months)):
        return HttpResponseNotFound("Invalid month<br><br>Yes invalid!")
    redirect_month = months[month-1]

    redirect_path = reverse("month-challenge",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html",{
            "text": challenge_text,
            "month_name": month
        })

    except:
        raise Http404()

def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())

    return render(request,"challenges/index.html",{
        "months":months
    })
    # for month in months:
    #     month_path = reverse("month-challenge",args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"
    
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)