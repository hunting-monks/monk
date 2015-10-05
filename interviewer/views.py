from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import UploadedFile
from django.db.models import Q
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from interview_track.logic import applicationcase
from interview_track.logic import interview
from interview_track.models import ApplicationCase
from interview_track.models import Interview
from interview_track.models import APPLICATION_STATUS_DICT
from interview_track.models import APPLICATION_STATUS_MAP
from interview_track.models import INTERVIEW_STATUS_DICT
from interview_track.models import INTERVIEW_STATUS_MAP

@login_required
def dashboard(request):
    interviews_pending = interview.get_interviews_by_user(
        request.user.id, [Q(status__lt=INTERVIEW_STATUS_MAP['Passed'])])
    interviews_closed = interview.get_interviews_by_user(
        request.user.id, [Q(status__gte=INTERVIEW_STATUS_MAP['Passed'])])
    return render_to_response(
            'interviewer_home.html',
            {'interviews_pending': interviews_pending,
             'interviews_closed': interviews_closed,
             'interview_status': INTERVIEW_STATUS_DICT},
            context_instance=RequestContext(request))


@login_required
def case_detail(request, case_id):
    appcase = ApplicationCase.objects.get(pk=case_id)
    interviews = Interview.objects.filter(case_id=appcase.id)
    return render(
        request,
        'interviewer_case_detail.html',
        {'case': appcase,
         'interviews': interviews,
         'interview_status': INTERVIEW_STATUS_DICT})