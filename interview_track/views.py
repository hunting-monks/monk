import urllib

from django.http import Http404
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import TemplateDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.conf import settings

def home_view(request, action=None):
    return render_to_response(
                'index.html',
                {'title': 'testtest'},
                context_instance=RequestContext(request))


class static_view(TemplateView):
    def get(self, request, page, *args, **kwargs):
        self.template_name = page
        response = super(static_view, self).get(request, *args, **kwargs)
        try:
            return response.render()
        except TemplateDoesNotExist:
            raise Http404()
