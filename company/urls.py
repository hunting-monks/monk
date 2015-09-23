from django.conf.urls import include, patterns
from django.conf.urls import url

from views import add_candidates
from views import add_jobs
from views import candidate_detail
from views import job_detail
from views import list_candidates
from views import list_jobs

urlpatterns = patterns('',
# candidate pages
    url(r'^add_candidates', add_candidates, name='add_candidates'),
    url(r'^candidate_detail/(?P<cid>\w+)/', candidate_detail, name='candidate_detail'),
    url(r'^list_candidates', list_candidates, name='list_candidates'),
# job pages
    url(r'^add_jobs', add_jobs, name='add_jobs'),
    url(r'^job_detail/(?P<cid>\w+)/', job_detail, name='job_detail'),
    url(r'^list_jobs', list_jobs, name='list_jobs'),
)
