from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import NewEmployee

class ViewTests(TestCase):

	def test_forms_dashboard(self):
		response = self.client.get(reverse('forms'))
		self.assertEqual(response.status_code, 302)