from django.shortcuts import render_to_response
from django import forms
import os.path
from facebook.models import facebook
import random

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

def home(request):
	sitetitle = 'Beauty around Us'
	headname = 'Beauty around Us'
	print request
	return render_to_response('index.html',locals())

def votea(request):
	sitetitle = 'Beauty around Us'
	headname = 'Beauty around Us'
	girlA = '12.jpg'
	girlB = '4886691_orig.jpg'
	print request
	print request.path
	print "--------"
	print request.GET
	print "--------"
	print request.POST
	print "--------"
	if request.path == '/votea/':
		print "it is "
	return render_to_response('vote.html',locals())

def vote(request):
	sitetitle = 'Beauty around Us'
	headname = 'Beauty around Us'
	list = facebook.objects.order_by('id')
	all = -1
	for i in list:
		all = all+1
	print all
	num = random.randint(0,all)
	num2 = random.randint(0,all)
	while num2 == num:
		num2 = random.randint(0,all)
	name = facebook.objects.get(id = list[num].id)
	name2 = facebook.objects.get(id = list[num2].id)
	girlA = str(name.filename)
	girlB = str(name2.filename)
	return render_to_response('vote.html',locals())
	
	
def upload(request):
	""" Function doc

	@param PARAM: DESCRIPTION
	@return RETURN: DESCRIPTION
	"""
	if request.method == 'POST':
		sitetitle = 'Beauty around Us'
		headname = 'Beauty around Us'
		print request.FILES['image']
		
		f = request.FILES['image']

		fn = f.name
		print fn
		aa = request.POST.values()
		print aa[1]
		name = facebook.objects.create(name = aa[1],desc=aa[2],filename=fn )

		print name.name
		print name.desc

		
				
		
		destination = open( PROJECT_PATH +'/media/image/' + fn , 'w')
		
		for chunk in f.chunks():
			destination.write(chunk)
		destination.close()
		return render_to_response('uploaded.html',locals())
		
		
		
	else:
				
		sitetitle = 'Beauty around Us'
		headname = 'Beauty around Us'
		return render_to_response('upload.html',locals())

