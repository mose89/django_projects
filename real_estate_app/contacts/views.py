from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contact

# Create your views here.
def contact(request):
	if request.method == 'POST':
		listing_id = request.POST['listing_id']
		listing = request.POST['listing']
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		user_id = request.POST['user_id']
		realtor_email = request.POST['realtor_email']

		contact = Contact(listing=listing, listing_id=listing_id\
			, name=name, email=email, phone=phone,\
			message=message, user_id=user_id, realtor_email=realtor_email)
		contact.save()

		send_mail(
		    'Inquiry from '+ name,
		    'Log in to your admin panel to see message.',
		    email,
		    [realtor_email],
		    fail_silently=False,
)

		messages.success(request, "Your request has been submitted. A Realtor will contact you shortly.")
	return redirect('/listings/'+listing_id)