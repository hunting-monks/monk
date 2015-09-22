from django.conf.urls import include, patterns
from django.conf.urls import url

from views import add_candidates
from views import candidate_detail
from views import list_candidates

urlpatterns = patterns('',
    url(r'^add_candidates', add_candidates, name='add_candidates'),
    url(r'^candidate_detail/(?P<cid>\w+)/', candidate_detail, name='candidate_detail'),
    url(r'^list_candidates', list_candidates, name='list_candidates'),
)
