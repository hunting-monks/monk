import logging
import re
from django import forms
from django.contrib.auth.models import User

LOGGER = logging.getLogger('accounts.forms')

class CompanyRegistrationForm(forms.Form):
	password = forms.CharField(widget=forms.PasswordInput(), label="Password")
	email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': ''}))
	name = forms.CharField()
	phone = forms.CharField()
	size = forms.IntegerField(min_value=1)
	zipCode = forms.CharField()
	terms = forms.BooleanField(widget=forms.CheckboxInput(),
							 label=(u'I agree to the Terms of Service'),
							 error_messages={'required': ("You must agree to the terms.")})

	def clean_email(self):
		value = self.data['email']
		if User.objects.filter(email=value, is_active=True).count():
			raise forms.ValidationError("This email is already registered.")

		user = None
		if value:
			try:
				user = User.objects.get(username=value, is_active=True)
			except (User.DoesNotExist,User.MultipleObjectsReturned):
				try:
					user = User.objects.get(email=value, is_active=True)
				except (User.DoesNotExist,User.MultipleObjectsReturned):
					pass
		if user:
			raise forms.ValidationError('Account already exists, please login <a href="/accounts/login">here</a>.')
		return value

	def clean_companyZip(self):
		if not re.match(r'\d\d\d\d\d$', self.data['zipCode']):
			raise forms.ValidationError('Please enter a valid zip code')
		return self.data['zipCode']

	def clean_companyPhone(self):
		if not re.match(r'^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$', self.data['phone']):
			raise forms.ValidationError('Please enter 10-digit phone number')

		return re.sub(r"[^\d]+", "", self.data['phone'])

	def clean_regEmployeeCount(self):
		try:
			if not int(self.data['size']) > 0:
				raise forms.ValidationError('Please enter a valid employee count')
			return self.data['size']
		except:
			raise forms.ValidationError('Please enter a valid employee count')


class InterviewerRegistrationForm(forms.ModelForm):
	password1 = forms.CharField(widget=forms.PasswordInput(), label="Password")
	password2 = forms.CharField(widget=forms.PasswordInput(), label="Repeat your password")
	email = forms.EmailField(widget = forms.EmailInput(attrs={'autofocus': ''}))
	terms = forms.BooleanField(widget=forms.CheckboxInput(),
							 label=(u'I agree to the Terms of Service'),
							 error_messages={'required': ("You must agree to the terms.")})

	def clean_password1(self):
		if self.data['password1'] != self.data['password2']:
			raise forms.ValidationError('Passwords are not the same')
		return self.data['password1']

	def clean_email(self):
		value = self.data['email']
		if User.objects.filter(email=value, is_active=True).count():
			raise forms.ValidationError("This email is already registered.")
		return value

	class Meta:
		model = User
		fields = ()


