from django.conf.urls import include, patterns
from django.conf.urls import url

from views import add_candidates
from views import add_case
from views import add_jobs
from views import add_scorecard_template
from views import candidate_detail
from views import dashboard
from views import case_detail
from views import interviewer_detail, recruiter_detail
from views import job_detail
from views import list_candidates
from views import list_cases
from views import InterviewerListView, EmployeeCreate, EmployeeUpdate, RecruiterListView
from views import list_jobs
from views import scorecard_template_detail


urlpatterns = patterns('',
# dashboard
    url(r'^home', dashboard, name='recruiter_dashboard'),
# API
    url(r'api/', include("company.API.urls")),

# cadidates pages
    url(r'^add_candidates', add_candidates, name='add_candidates'),
    url(r'^candidate_detail/(?P<cid>\w+)/', candidate_detail, name='candidate_detail'),
    url(r'^list_candidates', list_candidates, name='list_candidates'),
# job pages
    url(r'^add_jobs', add_jobs, name='add_jobs'),
    url(r'^job_detail/(?P<jobid>\w+)/', job_detail, name='job_detail'),
    url(r'^list_jobs', list_jobs, name='list_jobs'),

# employee pages
    url(r'^add_employees', EmployeeCreate.as_view(), name='add_employees'),
    url(r'^interviewer_detail/(?P<interviewer_id>\w+)/', interviewer_detail, name='interviewer_detail'),
    url(r'^recruiter_detail/(?P<recruiter_id>\w+)/', recruiter_detail, name='recruiter_detail'),
    url(r'^list_interviewers', InterviewerListView.as_view(), name='list_interviewers'),
    url(r'^list_recruiters', RecruiterListView.as_view(), name='list_recruiters'),

    url(r'^update_employee/(?P<employee_id>\w+)/', EmployeeUpdate.as_view(), name='update_employee'),
# interview pages
    url(r'^add_case', add_case, name='add_case'),
    url(r'^case_detail/(?P<case_id>\w+)/', case_detail, name='case_detail'),
    url(r'^list_cases', list_cases, name='list_cases'),
# scorecard pages
    url(r'^add_scorecard_template', add_scorecard_template, name='add_scorecard_template'),
    url(r'^scorecard_template_detail', scorecard_template_detail, name='scorecard_template_detail'),
)
