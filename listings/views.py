from django.shortcuts import render,get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger , Paginator
# Create your views here.
def index(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html',context)
def listing(request,listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listings': listing
    }
    return render(request, 'listings/listing.html',context)
def search(request):
    return render(request, 'listings/search.html')