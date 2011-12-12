#coding=utf-8
from django.shortcuts import render_to_response,redirect
from django import forms
import os.path
from facebook.models import facebook
from users.models import users
import random,string
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

import random,string
def random_word(num):
    w= ''
    seed = string.letters + string.digits
    for i in xrange(num):
        w+= seed[random.randrange(1,len(seed))] 
    return w

def home(request):
	sitetitle = 'Beauty around Us'
	headname = 'Beauty around Us'
	return render_to_response('index.html',locals())	

def vote(request):
	sitetitle = 'Beauty around Us'
	headname = 'Beauty around Us'
	print request.META['PATH_INFO']
	if '/votea/' == request.META['PATH_INFO']:
		
		username = request.COOKIES['csrftoken']
		username = username[0:20]
		choose = users.objects.get(name = username)
		
		print choose.filename
		
		girla = facebook.objects.get(id = choose.filename)
		print girla.rates
		print type(girla.rates)
		girla.rates = int(girla.rates) + 1
		girla.save()
		
		users(id = choose.id ).delete()
		return redirect('/vote/')
	elif '/voteb/' == request.META['PATH_INFO']:
		username = request.COOKIES['csrftoken']
		username = username[0:20]
		choose = users.objects.get(name = username)
		girla = facebook.objects.get(id = choose.filename2)
		print girla.rates
		print type(girla.rates)
		girla.rates = int(girla.rates) + 1
		girla.save()
		users(id = choose.id ).delete()
		return redirect('/vote/')
	else:
		print "ok"
		list = facebook.objects.order_by('id')
		all = facebook.objects.order_by('id').count()
		all = all-1
		num = random.randint(0,all)
		num2 = random.randint(0,all)
		while num2 == num:
			num2 = random.randint(0,all)
		name = facebook.objects.get(id = list[num].id)
		name2 = facebook.objects.get(id = list[num2].id)
		file = str(name.id)
		file2 = str(name2.id)
		girlA = str(name.filename)
		girlB = str(name2.filename)
		
		print request.COOKIES['csrftoken']
		username = request.COOKIES['csrftoken']
		username = username[0:20]
		try:
			choose = users.objects.get(name = username)
			users(id = choose.id ).delete()
		except:
			print "ok"
		user = users.objects.create(name = username,filename=file,filename2=file2)

		return render_to_response('vote.html',locals())
	
	
def upload(request):
	""" Function doc

	@param PARAM: DESCRIPTION
	@return RETURN: DESCRIPTION
	"""
	if request.method == 'POST':
		sitetitle = 'Beauty around Us'
		headname = 'Beauty around Us'
		print request.FILES
		f = request.FILES['image']
		fn = random_word(20)
		aa = request.POST['girlname']
		bb = request.POST['description']
		name = facebook.objects.create(name = aa,desc=bb,filename=fn,rates=0 )
		destination = open( PROJECT_PATH +'/media/image/' + fn , 'w')
		for chunk in f.chunks():
			destination.write(chunk)
		destination.close()
		done = str(fn)
		return render_to_response('uploaded.html',locals())
		
		
		
	else:
				
		sitetitle = 'Beauty around Us'
		headname = 'Beauty around Us'
		return render_to_response('upload.html',locals())
		
		
def about(request):
		sitetitle = 'Beauty around Us'
		headname = 'Beauty around Us'
		return render_to_response('about.html',locals())

def top(request):
		sitetitle = 'Beauty around Us'
		headname = 'Beauty around Us'
		list = facebook.objects.order_by('-rates')
		print list[0].rates
		no1 = list[0].filename
		no2 = list[1].filename
		no3 = list[2].filename
		no4 = list[3].filename
		no5 = list[4].filename
		no6 = list[5].filename
		no7 = list[6].filename
		no8 = list[7].filename
		return render_to_response('top.html',locals())
