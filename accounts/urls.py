from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from .forms import CompanyRegistrationForm, InterviewerRegistrationForm
from .views import CompanyRegistrationView, InterviewerRegistrationView

urlpatterns = patterns('',

	# customize user registration form
	url(r'^register/$',
		CompanyRegistrationView.as_view(
			template_name='registration/registration_company_form.html',
			form_class=CompanyRegistrationForm,
			success_url='/recruiter/home'
		),
		name='registration_register'
	),
	url(r'^register/done/$', 'accounts.views.register_done'),
	url(r'^activate/(?P<activation_key>\w+)/$',
		InterviewerRegistrationView.as_view(
			template_name='registration/registration_interviewer_form.html',
			form_class=InterviewerRegistrationForm,
			success_url='/interviewer/home'
		),
		name='registration_activate'
	),

	url(r'^register/closed/$',
                           TemplateView.as_view(template_name='registration/registration_closed.html'),
                           name='registration_disallowed'),

	(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/accounts/login/'}),

	(r'', include('registration.backends.simple.urls')),

)

