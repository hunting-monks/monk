from django.conf.urls import patterns, include, url
from .forms import CompanyRegistrationForm, LongAuthenticationForm
from .views import RegistrationView

urlpatterns = patterns('',

	# customize user registration form
	url(r'^register/$',
		RegistrationView.as_view(
			template_name='registration/registration_form.html',
			form_class=CompanyRegistrationForm,
			success_url='/dashboard/#/first'
		),
		name='registration_register'
	),
	url(r'^register/done/$', 'accounts.views.register_done'),

	(r'^login/$', 'accounts.views.login', {'authentication_form': LongAuthenticationForm}),

	#(r'^logout/$', 'accounts.views.logout', {'next_page': '/'}),
	#(r'^verify/$', 'accounts.views.verify'),
	#(r'^password/reset/$', 'django.contrib.auth.views.password_reset', {'password_reset_form': NewPasswordResetForm}),
	#(r'^resend/$', 'accounts.views.resend_registration_email'),
	# (r'^check-email/$', 'accounts.views.check_email'),

	(r'', include('registration.backends.simple.urls'))
)
