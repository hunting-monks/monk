"""monk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from views import home_view
from views import static_view

import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
# account management
    url(r'^accounts/logout', 'django.contrib.auth.views.logout',
        {'next_page': '/accounts/login'},
        name="logout"),
    url(r'^accounts/', include('registration.backends.default.urls')),
# recruiter pages
    url(r'^recruiter/', include("company.urls")),

    url(r'^$', home_view, name='home'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.MEDIA_ROOT, }),

    url(r'^(?P<page>.+\.html)$', static_view.as_view())
]
