from django.conf.urls import include, patterns
from django.conf.urls import url

from views import company_detail
from views import list_company


urlpatterns = patterns(
    '',
    url(r'^company_detail/(?P<pk>[0-9]+)/$', company_detail),
    url(r'^companies/$', list_company))
