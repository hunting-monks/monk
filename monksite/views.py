import urllib

from django.http import Http404
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import TemplateDoesNotExist
from django.views.generic import TemplateView


def home_view(request, action=None):
    if request.user.is_authenticated():
        return render_to_response(
                'recruiter_home.html',
                {'title': 'testtest'},
                context_instance=RequestContext(request))
    else:
        return redirect('/accounts/login')


class static_view(TemplateView):
    def get(self, request, page, *args, **kwargs):
        self.template_name = page
        response = super(static_view, self).get(request, *args, **kwargs)
        try:
            return response.render()
        except TemplateDoesNotExist:
            raise Http404()
