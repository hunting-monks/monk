import logging
from django.shortcuts import render
from registration.views import RegistrationView as BaseRegistrationView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from registration import signals
from company.models import Company

log = logging.getLogger(__name__)

SESSION_INITIAL_EMAIL_KEY = "_initEmail"


class RegistrationView(BaseRegistrationView):

    def register(self, request, form):
        username = form.cleaned_data['email']
        password = form.cleaned_data['password']
        zipcode = form.cleaned_data['zipCode']
        phone = form.cleaned_data['phone']
        size = form.cleaned_data['size']
        name = form.cleaned_data['name']

        User.objects.create_user(username, email=username, password=password)
        new_user = authenticate(
			username=username,
			password=password
		)
        login(request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)

        import pdb; pdb.set_trace()
        Company.register_company(new_user, name, zipCode=zipcode, phone=phone, size=size)
        return new_user


def register_done(request, template_name='registration/registration_done.html'):
    return render(request, template_name, {})
