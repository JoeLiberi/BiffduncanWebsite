from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import loader, Context
from django.contrib.auth.decorators import login_required
from customerportal.models import NewEmployee
from .forms import NewEmployeeForm
from django.core.urlresolvers import reverse


@login_required(login_url='/login/')
def dashboard(request):
	try:
		employees = NewEmployee.objects.all().order_by('created')

		context = {
			'employees': employees
		}
	except:
		context = {
			'employees': 'no employees created'
		}

	return render(request, 'dashboard.html', context)

@login_required(login_url='/login/')
def forms_dashboard(request):

	create_form = NewEmployeeForm()
	if request.method == 'GET':

		try:
			form_list = NewEmployee.objects.all().order_by('created')
			context = {
				'form_list': form_list,
				'create_form': create_form
			}

		except:
			context = {
				'form_list': None,
				'create_form': create_form
			}

		return render(request, 'forms_dashboard.html', context)

	elif request.method == 'POST':
		form = NewEmployeeForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('dashboard') )

		else:
			context = {
				'form': form
			}

		return render(request, 'forms_dashboard.html', context)
	# if request.method == 'POST' and form.is_valid():
	# 	form.save()
	# 	return HttpResponseRedirect('/dashboard')
