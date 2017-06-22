from django.shortcuts import render
from django.template import loader, Context
from .models import Aboutus

def index(request):
	template = loader.get_template('aboutus.html')
	try:
		aboutus_txt = Aboutus.objects.all()[0]
	except:
		# This will return nothing
		aboutus_txt = Aboutus.objects.all()

	context = {
		'aboutus' : aboutus_txt
	}
	return render(request, 'aboutus.html', context)