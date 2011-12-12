from django.db import models

class users(models.Model):
	""" Class doc """
	
	name = models.CharField(max_length=1000)
	filename = models.CharField(max_length=1000)
	filename2 = models.CharField(max_length=1000)
	ip = models.IPAddressField(blank=True, null=True)
	meta =  models.TextField(blank=True, null=True)
	
	def __unicode__(self):
		return self.ip

