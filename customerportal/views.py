from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Context
from django.contrib.auth.decorators import login_required
from customerportal.models import NewEmployee
from .forms import NewEmployeeForm

@login_required(login_url='/login/')
def index(request):
	context = {
		'test': "This is a placeholder"
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

	if request.method == 'POST' and form.is_valid():
		form.save()
		return HttpResponseRedirect('/dashboard')

	return render(request, 'forms_dashboard.html', context)
