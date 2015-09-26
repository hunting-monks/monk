import urllib
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import TemplateDoesNotExist
from django.views.generic import TemplateView

from company.logic import employee

@login_required
def home_view(request):
    role = employee.get_user_role(request.user.id)
    if role == 'Recruiter':
        return redirect('/recruiter/home')
    elif role == 'Interviewer':
        return redirect('/interviewer/home')
    else:
        return redirect('/recruiter/home')  # hack: will have a default dashboard


class static_view(TemplateView):
    def get(self, request, page, *args, **kwargs):
        self.template_name = page
        response = super(static_view, self).get(request, *args, **kwargs)
        try:
            return response.render()
        except TemplateDoesNotExist:
            raise Http404()
