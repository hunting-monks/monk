from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import UploadedFile
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import ApplicantForm
from forms import EmployeeForm
from forms import JobForm
from interview_track.models import Job
from logic import applicant
from logic import employee
from logic import job
from models import Applicant
from models import Employee


'''functions for rendering candidate pages'''
@login_required
def list_candidates(request):
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
        form = JobForm()
    return render(
        request,
        'add_job.html',
        {'form': form, 'eid': emp.id, 'cid': emp.company.id})


@login_required
def list_jobs(request):
    jobs = []
    try:
        for j in job.get_jobs_by_user(request.user.id):
            jobs.append(model_to_dict(j))
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
                return render(request, 'interviewer_detail.html', {'interviewer': interviewer})
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
    return render(request, 'interviewer_detail.html', {'interviewer': interviewer})
    return