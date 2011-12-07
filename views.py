from django.shortcuts import render_to_response


def home(request):
	sitetitle = 'Beauty around Us'
	headname = 'Beauty around Us'
	return render_to_response('index.html',locals())


def upload(request):
	""" Function doc

	@param PARAM: DESCRIPTION
	@return RETURN: DESCRIPTION
	"""
	sitetitle = 'Beauty around Us'
	headname = 'Beauty around Us'
	return render_to_response('upload.html',locals())

