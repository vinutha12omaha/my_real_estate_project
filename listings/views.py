from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator  ## For Pagination
from pages.models import TopBar


def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)  ## Check or uncheck in admin area
    tb = TopBar.objects.get()
    ### Pagination Start ###
    paginator = Paginator(listings, 6)   ## how much item i want to show in each page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    ### Pagination End ###

    context = {
        'listings': paged_listings,
        'tb': tb
    }

    return render(request, 'listings/listings.html', context)


##----## This is for single listing (More Info Button) ##----##
def listing(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)   ## if page doesn't exist, it will show page not found(error message)
    tb = TopBar.objects.get()
    context = {
        'listing': listing,
        'tb': tb
    }

    return render(request, 'listings/listing.html', context)
