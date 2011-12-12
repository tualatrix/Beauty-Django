from django.db import models

# Create your models here.
class facebook(models.Model):
	""" Class doc """
	
	name = models.CharField(max_length=30)
	desc = models.CharField(max_length=1000)
	filename = models.CharField(max_length=1000)
	votes =  models.IntegerField(max_length=100)
	show =  models.IntegerField(max_length=100)
	rate =  models.FloatField(max_length=100)
	uploader = models.IPAddressField(blank=True, null=True)
	meta =  models.TextField(blank=True, null=True)
	
	def __unicode__(self):
		return u'%s %s %s %s %s %s %s'%(self.name , self.desc , self.filename, self.votes, self.show, self.rate,self.uploader)

