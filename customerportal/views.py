from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Context
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
	context = {
		'text': "This is some text",
	}
	return render(request, 'customerportal.html', context)
