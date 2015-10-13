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

	# (r'^login/$', 'accounts.views.login', {'authentication_form': LongAuthenticationForm}),

	#(r'^logout/$', 'accounts.views.logout', {'next_page': '/'}),
	#(r'^verify/$', 'accounts.views.verify'),
	#(r'^password/reset/$', 'django.contrib.auth.views.password_reset', {'password_reset_form': NewPasswordResetForm}),
	#(r'^resend/$', 'accounts.views.resend_registration_email'),
	# (r'^check-email/$', 'accounts.views.check_email'),

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

	(r'', include('registration.backends.simple.urls')),

	# url(r'^login/$',
	#    auth_views.login,
	#    {'template_name': 'registration/login.html'},
	#    name='auth_login'),
	# url(r'^logout/$',
	#    auth_views.logout,
	#    {'template_name': 'registration/logout.html'},
	#    name='auth_logout'),
	# url(r'^password/change/$',
	#    auth_views.password_change,
	#    {'post_change_redirect': reverse_lazy('auth_password_change_done')},
	#    name='auth_password_change'),
	# url(r'^password/change/done/$',
	#    auth_views.password_change_done,
	#    name='auth_password_change_done'),
	# url(r'^password/reset/$',
	#    auth_views.password_reset,
	#    {'post_reset_redirect': reverse_lazy('auth_password_reset_done')},
	#    name='auth_password_reset'),
	# url(r'^password/reset/complete/$',
	#    auth_views.password_reset_complete,
	#    name='auth_password_reset_complete'),
	# url(r'^password/reset/done/$',
	#    auth_views.password_reset_done,
	#    name='auth_password_reset_done'),

)

