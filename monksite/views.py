import urllib
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import TemplateDoesNotExist
from django.views.generic import TemplateView


@login_required
def home_view(request, action=None):
    return redirect('/users/list_candidates')


class static_view(TemplateView):
    def get(self, request, page, *args, **kwargs):
        self.template_name = page
        response = super(static_view, self).get(request, *args, **kwargs)
        try:
            return response.render()
        except TemplateDoesNotExist:
            raise Http404()
