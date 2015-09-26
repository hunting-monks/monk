from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import UploadedFile
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext


@login_required
def dashboard(request):
    return render_to_response(
            'interviewer_home.html',
            context_instance=RequestContext(request))