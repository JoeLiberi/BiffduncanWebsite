from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Context

def index(request):
	context = {
		'text': "This is some text",
	}
	return render(request, 'customerportal.html', context)
