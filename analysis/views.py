from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse

def index(request):
	return render(request, 'analysis/index.html', {})
#	return HttpResponse("analysis page")
