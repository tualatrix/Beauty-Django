from django.db import models
from django.contrib import admin
# Create your models here.
class users(models.Model):
	""" Class doc """
	
	name = models.CharField(max_length=50000)
	filename = models.CharField(max_length=1000)
	filename2 = models.CharField(max_length=1000)
	
	def __unicode__(self):
		return self.name

admin.site.register((users))
