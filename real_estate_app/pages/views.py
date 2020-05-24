from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor


# Create your views here.

def index(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)
	context ={
	'listings': listings
	}
	return render(request, 'pages/index.html', context)

def about(request):
	realtors = Realtor.objects.order_by('-hire_date')
	#Get MVP
	mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
	context ={
	'realtors': realtors,
	'mvps': mvp_realtors
	}
	return render(request, 'pages/about.html', context)