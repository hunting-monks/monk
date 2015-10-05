from django.conf.urls import include, patterns
from django.conf.urls import url

from views import dashboard
from views import case_detail


urlpatterns = patterns('',
# dashboard
    url(r'^home', dashboard, name='interviewer_dashboard'),
    url(r'^case_detail/(?P<case_id>\w+)/', case_detail, name='interviewer_case_detail'),

)
