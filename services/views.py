from django.shortcuts import render
from django.template import loader, Context
from .models import Services

def index(request):
	template = loader.get_template('services.html')
	services_list = Services.get_all_services()
	context = {
		'services' : services_list
	}
	return render(request, 'services.html', context)