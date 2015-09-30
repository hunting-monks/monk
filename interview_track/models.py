from datetime import date
from datetime import datetime
from datetime import time
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey

from common import utils
from company.models import Applicant
from company.models import Company
from company.models import Employee
from company.models import INDUSTRY_CATEGORIES
from company.models import SKILL_LEVEL


APPLICATION_STATUS = (
    (1, 'Not started'),
    (2, 'Phone screen scheduled'),
    (3, 'Phone screen finished'),
    (4, 'Onsite scheduled'),
    (5, 'Onsite finished'),
    (6, 'Offered'),
    (7, 'Rejected'),
    (8, 'On hold'))
APPLICATION_STATUS_MAP = utils.list2dict_reverse(APPLICATION_STATUS)

INTERVIEW_CATEGORIES = (
    ('', 'Interview type'),
    (1, 'Phone screen'),
    (2, 'Onsite'),
    (3, 'Onsite with HR'),
    (4, 'Onsite with HM'))
INTERVIEW_CATEGORIES_MAP = utils.list2dict_reverse(INTERVIEW_CATEGORIES)

INTERVIEW_STATUS = (
    (1, 'Scheduled'),
    (2, 'Candidate Confirmed'),
    (3, 'Interviewer Confirmed'),
    (4, 'Passed'),
    (5, 'Rejected'))
INTERVIEW_STATUS_MAP = utils.list2dict_reverse(INTERVIEW_STATUS)


class Job(models.Model):

    company = models.ForeignKey(Company)
    title = models.CharField(max_length=50)
    area = models.IntegerField(choices=INDUSTRY_CATEGORIES)
    level = models.IntegerField(choices=SKILL_LEVEL)
    description = models.CharField(max_length=5000)
    salary_high = models.IntegerField(blank=True, default=0)
    salary_low = models.IntegerField(blank=True, default=0)

    creator = models.ForeignKey(Employee, related_name="creator")
    recruiter = models.ForeignKey(Employee, related_name="recruiter")
    hiring_manager = models.ForeignKey(Employee, related_name="hm")

    expire_date = models.DateField(blank=True, default=date.min)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%d: %s - %s" % (self.id, self.title, self.company)


class ApplicationCase(models.Model):
    class meta:
        unique_together = (("applicant", "job"))

    applicant = models.ForeignKey(Applicant)
    job = models.ForeignKey(Job)
    status = models.IntegerField(choices=APPLICATION_STATUS, default=APPLICATION_STATUS_MAP['Not started'])

    creator = models.ForeignKey(Employee)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return "%d: %s, %s" % (
            self.id, self.applicant.__unicode__(), self.job.__unicode__())


class Interview(models.Model):

    case = models.ForeignKey(ApplicationCase)
    interviewer = models.ForeignKey(Employee)
    category = models.IntegerField(choices=INTERVIEW_CATEGORIES)
    interview_date = models.DateField(default=date.min)
    start_time = models.TimeField(default=time.min)
    end_time = models.TimeField(default=time.min)
    status = models.IntegerField(choices=INTERVIEW_STATUS, default=INTERVIEW_STATUS_MAP['Scheduled'])
    comment = models.CharField(max_length=2000, blank=True, default="")
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class InterviewScore(models.Model):

    interview = models.ForeignKey(Interview)
    evaluated_field = models.CharField(max_length=50, blank=True, default="")
    score = models.IntegerField(blank=True, default=0)
    comment = models.CharField(max_length=2000, blank=True, default="")
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

