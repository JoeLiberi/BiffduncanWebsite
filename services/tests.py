from django.test import TestCase
from services.models import Services
from datetime import datetime

class ServicesTestCase(TestCase):

	def setUp(self):
		dt = datetime.now()
		dt1 = dt.replace(day=dt.day-1)
		dt2 = dt.replace(day=dt.day-2)

		Services.objects.create(title="Network Consulting", description='This is a test', created=dt1)
		Services.objects.create(title="VoIP Phone Systems", description='This is a test', created=dt2)

	def test_title_is_no_more_than_24_chars(self):
		"""Make sure the title isnt to long"""
		netc = Services.objects.get(title="Network Consulting")
		self.assertLess(len(netc.title), 24)

	def test_description_no_more_tan_120_chars(self):
		"""Make sure the descriptions is not more ath 120 chars"""
		netc = Services.objects.get(title="Network Consulting")
		self.assertLess(len(netc.description), 120)

	def test_order_by_created(self):
		""" Make sure the services are ordered by created when a query is made. """
		all_entries = Services.get_all_services()
		self.assertLess(all_entries[0].created, all_entries[1].created)


