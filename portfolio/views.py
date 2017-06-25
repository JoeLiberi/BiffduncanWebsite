from django.shortcuts import render
from django.template import loader, Context
from .models import Portfolio

def index(request):
	template = loader.get_template('portfolio.html')
	portfolio_list = Portfolio.get_all_services()
	context = {
		'portfolio' : portfolio_list,
	}
	return render(request, 'portfolio.html', context)