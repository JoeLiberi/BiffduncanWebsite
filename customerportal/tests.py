from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import NewEmployee
from django.test import Client

class ViewTests(TestCase):
	def setup(self):
		NewEmployee.objects.create(name='Joe', location='biffduncan')
		NewEmployee.objects.create(name='bob', location='biffduncan')
		NewEmployee.objects.create(name='dan', location='biffduncan')


	def test_login_required(self):
		response = self.client.get(reverse('forms'))
		self.assertEqual(response.status_code, 302)

	def test_forms_dashboard_html(self):
		response = self.client.post('/login/', {'username': 'test', 'password': 'test'})

		self.assertEqual(response.status_code, 200)

		response = self.client.get('/cportal/')


