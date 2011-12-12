#coding=utf-8
from __future__ import division
from django.shortcuts import render_to_response,redirect
from django import forms
import os.path
from facebook.models import facebook
from users.models import users
import random,string
import magic
import shutil
import os

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

import random,string
def random_word(num):
    w= ''
    seed = string.letters + string.digits
    for i in xrange(num):
        w+= seed[random.randrange(1,len(seed))] 
    return w

def home(request):
	sitetitle = 'Miss Beauty'
	headname = 'Miss Beauty'
	return render_to_response('index.html',locals())

def vote(request):
	if '/votea/' == request.META['PATH_INFO']:
		
		username = request.COOKIES['csrftoken']
		username = username[0:20]
		try:
			choose = users.objects.get(name = username)
		except:
			return redirect('/')
		
		print choose.filename
		
		girla = facebook.objects.get(id = choose.filename)
		girla.votes = girla.votes + 1
		girla.rate = girla.votes/girla.show
		girla.save()
		return redirect('/vote/')
	elif '/voteb/' == request.META['PATH_INFO']:
		username = request.COOKIES['csrftoken']
		username = username[0:20]
		try:
			choose = users.objects.get(name = username)
		except:
			return redirect('/')
		girla = facebook.objects.get(id = choose.filename2)
		girla.votes = girla.votes + 1
		girla.rate = girla.votes/girla.show
		girla.save()
		return redirect('/vote/')
	else:

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
		except:
			user = users.objects.create(name = username,filename=file,filename2=file2,ip=request.META['REMOTE_ADDR'],meta=request.META['HTTP_USER_AGENT'])
			name.show = name.show+1
			name.save()
			name2.show = name2.show+1
			name2.save()
			return render_to_response('vote.html',locals())
		showname = users.objects.get(name = username)
		showname.filename=file
		showname.filename2=file2
		showname.save()
		name.show = name.show+1
		name.save()
		name2.show = name2.show+1
		name2.save()

		return render_to_response('vote.html',locals())
	
	
def upload(request):
	if request.method == 'POST':
		sitetitle = 'Miss Beauty'
		headname = 'Miss Beauty'
		print request.FILES
		f = request.FILES['image']

		fn = random_word(20)
		aa = request.POST['girlname']
		bb = request.POST['description']
		destination = open( PROJECT_PATH +'/media/image/' + fn , 'w')
		for chunk in f.chunks():
			destination.write(chunk)
		destination.close()
		mime = magic.Magic(mime=True)
		if mime.from_file(PROJECT_PATH +'/media/image/' + fn ).split("/")[0] == "image":
			name = facebook.objects.create(name = aa,desc=bb,filename=fn,rate=0,votes=0,show=0,uploader=request.META['REMOTE_ADDR'],meta=request.META['HTTP_USER_AGENT'])
		else:
			os.remove(PROJECT_PATH +'/media/image/' + fn )
			return render_to_response('noupload.html',locals())
		done = str(fn)
		return render_to_response('uploaded.html',locals())
		
		
		
	else:
		return render_to_response('upload.html',locals())
		
		
def about(request):
		return render_to_response('about.html',locals())

def top(request):
		list = facebook.objects.order_by('-votes')
		no1 = list[0].filename
		no2 = list[1].filename
		no3 = list[2].filename
		no4 = list[3].filename
		no5 = list[4].filename
		no6 = list[5].filename
		no7 = list[6].filename
		no8 = list[7].filename
		return render_to_response('top.html',locals())

def rate(request):
		list = facebook.objects.order_by('-rate')
		no1 = list[0].filename
		no2 = list[1].filename
		no3 = list[2].filename
		no4 = list[3].filename
		no5 = list[4].filename
		no6 = list[5].filename
		no7 = list[6].filename
		no8 = list[7].filename
		return render_to_response('top.html',locals())
