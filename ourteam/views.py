from django.shortcuts import render
from django.template import loader, Context
from .models import Employees

def index(request):
	template = loader.get_template('ourteam.html')
	employees = Employee.objects.all()
	context = {
		'employees' : employees
	}
	return render(request, 'ourteam.html', context)