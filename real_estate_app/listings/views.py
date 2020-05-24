from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from datetime import datetime as dt
# Create your views here.
def index(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)
	paginator = Paginator(listings, 3)
	page = request.GET.get('page')
	paged_listings = paginator.get_page(page)
	context = {
	'listings': paged_listings
	}
	return render(request, 'listings/listings.html', context=context)

def listing(request, listing_id):
	listing = get_object_or_404(Listing, pk=listing_id)
	realtor = listing.realtor
	context = {
	'listing': listing,
	'realtor': realtor,
	'dt': dt
	}
	return render(request, 'listings/listing.html', context)

def search(request):
	return render(request, 'listings/search.html')