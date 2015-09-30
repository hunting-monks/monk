from functools import partial
from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import UploadedFile
from django.forms.models import modelformset_factory
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from common import utils
from forms import ApplicantForm
from forms import ApplicationCaseForm
from forms import EmployeeForm
from forms import JobForm
from interview_track.forms import InterviewForm
from interview_track.logic import applicationcase
from interview_track.models import ApplicationCase
from interview_track.models import Interview
from interview_track.models import Job
from logic import applicant
from logic import employee
from logic import job
from models import Applicant
from models import Employee


@login_required
def dashboard(request):
    cases = applicationcase.get_application_cases_by_uid(request.user.id)
    jobs = job.get_jobs_by_user(request.user.id)
    return render_to_response(
            'recruiter_home.html',
            {'cases': cases,
             'jobs': jobs},
            context_instance=RequestContext(request))


@login_required
def list_candidates(request):
    """functions for rendering candidate pages"""
    candidates = []
    try:
        emp = employee.get_employee_by_user(request.user.id)
        for c in applicant.get_applicants_by_creator(employee_id=emp.id):
            candi = model_to_dict(c)
            if not candi['photo']:
                candi['photo'] = 'avartars/avartar_default.jpg'
            candidates.append(candi)
    except Exception as ex:
        print ex
        pass
    return render_to_response(
            'list_candidates.html',
            {'candidates': candidates},
            context_instance=RequestContext(request))


@login_required
def add_candidates(request):
    eid = employee.get_employee_by_user(request.user.id).id
    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                candi = form.save()
                return render(request, 'candidate_detail.html', {'candi': candi})
            except Exception as ex:
                print ex
    else:
        form = ApplicantForm()

    return render(request, 'add_candidates.html', {'form': form, 'eid': eid})


@login_required
def candidate_detail(request, cid):
    candidate = Applicant.objects.get(pk=cid)
    return render(request, 'candidate_detail.html', {'candi': candidate})


'''functions for rendering job pages'''
@login_required
def add_jobs(request):
    emp = employee.get_employee_by_user(userid=request.user.id)
    if request.method == 'POST':
        form = JobForm(request.POST, cid=emp.company.id)
        if form.is_valid():
            try:
                job = form.save()
                return render(request, 'job_detail.html', {'job': job})
            except Exception as ex:
                print ex
    else:
        form = JobForm(cid=emp.company.id)
    return render(
        request,
        'add_job.html',
        {'form': form, 'cid': emp.company.id, 'eid': emp.id})


@login_required
def list_jobs(request):
    jobs = []
    try:
        jobs = job.get_jobs_by_user(request.user.id)
    except Exception as ex:
        print ex
        pass
    return render_to_response(
            'list_jobs.html',
            {'jobs': jobs},
            context_instance=RequestContext(request))


@login_required
def job_detail(request, jobid):
    job = Job.objects.get(pk=jobid)
    return render(request, 'job_detail.html', {'job': job})


'''functions for rendering interviewer pages'''
@login_required
def add_interviewers(request):
    emp = employee.get_employee_by_user(userid=request.user.id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                interviewer = form.save()
                return render(
                    request,
                    'interviewer_detail.html',
                    {'interviewer': interviewer})
            except Exception as ex:
                print ex
    else:
        form = EmployeeForm()
    return render(
        request,
        'add_interviewer.html',
        {'form': form, 'cid': emp.company.id})


@login_required
def list_interviewers(request):
    interviewers = []
    try:
        for j in employee.get_interviewers_by_recruiter(request.user.id):
            interviewers.append(model_to_dict(j))
    except Exception as ex:
        print ex
        pass
    return render_to_response(
            'list_interviewers.html',
            {'interviewers': interviewers},
            context_instance=RequestContext(request))


@login_required
def interviewer_detail(request, jobid):
    interviewer = Employee.objects.get(pk=jobid)
    return render(
        request,
        'interviewer_detail.html',
        {'interviewer': interviewer})


MAX_NUM_INTERVIEW = 3
'''functions for rendering interview case pages'''
@login_required
def add_case(request):
    emp = employee.get_employee_by_user(userid=request.user.id)
    InterviewFormSet = modelformset_factory(
        Interview,
        form=utils.gen_class_with_kwargs(InterviewForm, eid=emp.id),
        extra=MAX_NUM_INTERVIEW)
    if request.method == 'POST':
        form = ApplicationCaseForm(request.POST)
        if form.is_valid():
            try:
                form = form.save()
                iforms = InterviewFormSet(request.POST)
                cnt = 0
                for iform in iforms:
                    iform.data['form-%d-case' % (cnt,)] = form.id
                    cnt += 1
                if iforms.is_valid():
                    iforms = iforms.save()
                    return render(
                        request,
                        'case_detail.html',
                        {'case': form, 'interviews': iforms})
            except Exception as ex:
                print ex
    else:
        form = ApplicationCaseForm()
        iforms = InterviewFormSet(queryset=Interview.objects.none())
    return render(
        request,
        'add_case.html',
        {'eid': emp.id, 'form': form, 'iforms': iforms})


@login_required
def list_cases(request):
    cases = []
    try:
        cases = applicationcase.get_application_cases_by_uid(request.user.id)
    except Exception as ex:
        print ex
    return render_to_response(
            'list_cases.html',
            {'cases': cases},
            context_instance=RequestContext(request))


@login_required
def case_detail(request, case_id):
    appcase = ApplicationCase.objects.get(pk=case_id)
    interviews = Interview.objects.filter(case_id=appcase.id)
    return render(
        request,
        'case_detail.html',
        {'case': appcase,
         'interviews': interviews})

