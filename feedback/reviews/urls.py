from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path("",views.review),
    path("thank-you",views.thank_you)
]
