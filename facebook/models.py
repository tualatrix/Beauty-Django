from django.db import models
from django.contrib import admin
# Create your models here.
class facebook(models.Model):
	""" Class doc """
	
	name = models.CharField(max_length=30)
	desc = models.CharField(max_length=100)
	filename = models.CharField(max_length=1000)
	rates =  models.IntegerField(max_length=100)
	
	def __unicode__(self):
		return self.name

admin.site.register((facebook))
