from django.conf.urls import include, patterns
from django.conf.urls import url

from views import dashboard

urlpatterns = patterns('',
# dashboard
    url(r'^home', dashboard, name='interviewer_dashboard'),
)
