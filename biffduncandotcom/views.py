from django.shortcuts import render
from django.template import loader, Context
from services.models import Services
from portfolio.models import Portfolio
from aboutus.models import Aboutus
from ourteam.models import Employee
from contactus.models import ContactUs
from contactus.forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
import sendgrid
import os
from sendgrid.helpers.mail import *

def index(request):
	services_list = Services.get_all_services()
	template = loader.get_template('base.html')
	portfolio_list = Portfolio.get_all_services()
	employees = Employee.objects.all()
	form_class = ContactForm

	try:
		aboutus_txt = Aboutus.objects.all()[0]
	except:
		# This will return nothing
		aboutus_txt = Aboutus.objects.all()

	""" Logic for Email """
	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get('contact_name', '')
			contact_email = request.POST.get('contact_email', '')
			contact_phone = request.POST.get('contact_phone', '')
			form_content = request.POST.get('content', '')

			# Email the profile with the 
			# contact information
			# template = get_template('contact_template.txt')
			context = Context({
				'contact_name': contact_name,
				'contact_email': contact_email,
				'contact_phone': contact_phone,
				'form_content': form_content,
				})

			content = template.render(context)

			# email = EmailMessage(
			# 	"New contact form submission",
			# 	content,
			# 	"Your website" +'',
			# 	['info@biffduncan.com'],
			# 	headers = {'Reply-To': contact_email }
			# 	)
			# email.send()
			# return redirect('#')
			
			sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('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'))
			from_email = Email("website@biffduncan.com")
			subject = "New Customer Inquery"
			to_email = Email("info@biffduncan.com")
			mail = Mail(from_email, subject, to_email, content)
			response = sg.client.mail.send.post(request_body=mail.get())

	context = {
		'services' : services_list,
		'portfolio' : portfolio_list,
		'aboutus' : aboutus_txt,
		'employees' : employees,
		'form' : form_class
	}
	return render(request, 'base.html', context)
	# return render_to_response(template='base.html',)