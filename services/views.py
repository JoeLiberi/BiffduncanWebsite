# from django.shortcuts import render
# from django.template import loader, Context
# from .models import Services

# def index(request):
# 	template = loader.get_template('base.html')
# 	services_list = Services.get_all_services()
# 	context = {
# 		'services' : services_list
# 	}
# 	return render(request, 'base.html', context)
# 	# return render_to_response(template='base.html',)