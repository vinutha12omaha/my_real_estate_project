from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from .models import TopBar

# Create your views here.

def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    tb = TopBar.objects.get()

    context = {
        'listings': listings,
        'tb': tb
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get MVP (Seller of the month)
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    tb = TopBar.objects.get()

    context = {
        'mvp_realtors': mvp_realtors,
        'tb': tb
    }

    return render(request, 'pages/about.html', context)