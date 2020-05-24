from django.db import models
from datetime import datetime as dt
# Create your models here.
class Realtor(models.Model):
	name = models.CharField(max_length = 150)
	photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
	description = models.TextField()
	email = models.CharField(max_length = 100)
	phone = models.CharField(max_length = 50)
	is_mvp = models.BooleanField(default = False)
	hire_date = models.DateTimeField(default=dt.now, blank=True)

	def __str__(self):
		return self.name