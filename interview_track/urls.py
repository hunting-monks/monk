from django.conf.urls import include, patterns
from django.conf.urls import url

from views import home_view
from views import static_view


urlpatterns = patterns('',
    url(r'^$', home_view, name='home'),
)
