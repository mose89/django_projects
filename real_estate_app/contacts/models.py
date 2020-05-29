from django.db import models
from datetime import datetime as dt

# Create your models here.

class Contact(models.Model):
	"""docstring for contacts"""
	listing = models.CharField(max_length = 200)
	listing_id = models.IntegerField()
	name = models.CharField(max_length = 100)
	email = models.CharField(max_length = 100)
	phone = models.CharField(max_length = 100)
	message = models.TextField(blank=True, max_length = 750)
	contact_date = models.DateTimeField(blank=True, default = dt.now)
	user_id = models.IntegerField(blank=True)

	def __str__(self):
		return self.name