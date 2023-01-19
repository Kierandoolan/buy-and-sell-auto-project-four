from django.shortcuts import render
from django.views import generic
from .models import CarAd


class CarAdList(generic.ListView):
    """
    Shows maximum of six Car Posts
    on the index.html page
    """
    model = CarAd
    queryset = CarAd.objects.order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6
