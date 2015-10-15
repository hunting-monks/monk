from django.test import TestCase

class ListViewTest(TestCase):

	def test_add_employees(self):
		# correct_list = List.objects.create()
		response = self.client.get('/recruiter/add_employees/')
		print response


