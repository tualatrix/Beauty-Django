#coding=utf-8
from django.shortcuts import render_to_response,redirect
from django import forms
import os.path
from facebook.models import facebook
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
	if 'fileid' in request.POST:
		whatid = request.POST['fileid']
		votes = facebook.objects.get(id = whatid )
		votes.rates =  int(votes.rates) + 1
		vote = str(votes.rates)
		votes.save()
		return redirect('/vote/')
	elif 'fileid2' in request.POST:
		whatid = request.POST['fileid2']
		votes = facebook.objects.get(id = whatid )
		votes.rates =  int(votes.rates) + 1
		vote = str(votes.rates)
		votes.save()
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

