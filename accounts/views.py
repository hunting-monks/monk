from django.conf import settings
import logging
from django.shortcuts import render
from registration.views import RegistrationView as BaseRegistrationView, ActivationView as BaseActivationView
from registration.models import RegistrationProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from registration import signals
from company.models import Company

log = logging.getLogger(__name__)

SESSION_INITIAL_EMAIL_KEY = "_initEmail"


class CompanyRegistrationView(BaseRegistrationView):

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

        Company.register_company(new_user, name, zipCode=zipcode, phone=phone, size=size)
        return new_user

    def registration_allowed(self, request):
        """
        Indicate whether account registration is currently permitted,
        based on the value of the setting ``REGISTRATION_OPEN``. This
        is determined as follows:
        * If ``REGISTRATION_OPEN`` is not specified in settings, or is
          set to ``True``, registration is permitted.
        * If ``REGISTRATION_OPEN`` is both specified and set to
          ``False``, registration is not permitted.
        """
        return getattr(settings, 'REGISTRATION_OPEN', True)


class InterviewerRegistrationView(BaseRegistrationView):

    def register(self, request, form):
        username = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        oldUserKey = self.kwargs['activation_key']
        oldUser = User.objects.get(username=oldUserKey)

        employee = oldUser.employee
        User.objects.create_user(username, email=username, password=password)
        new_user = authenticate(
			username=username,
			password=password
		)
        login(request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)

        employee.user = new_user
        employee.save()
        oldUser.delete()
        return new_user

    def registration_allowed(self, request):
        """
        Indicate whether account registration is currently permitted,
        based on the value of the setting ``REGISTRATION_OPEN``. This
        is determined as follows:
        * If ``REGISTRATION_OPEN`` is not specified in settings, or is
          set to ``True``, registration is permitted.
        * If ``REGISTRATION_OPEN`` is both specified and set to
          ``False``, registration is not permitted.
        """
        return getattr(settings, 'REGISTRATION_OPEN', True)


def register_done(request, template_name='registration/registration_done.html'):
    return render(request, template_name, {})




