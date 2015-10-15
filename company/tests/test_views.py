from django.test import TestCase

class ListViewTest(TestCase):

	def test_add_interviewer(self):
		# correct_list = List.objects.create()
		response = self.client.get('/recruiter/add_interviewers/')
		print response


