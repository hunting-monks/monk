from django.conf.urls import include, patterns
from django.conf.urls import url

from views import candidate_list

urlpatterns = patterns('',
    url(r'^candidate_list', candidate_list, name='candidates'),
)
