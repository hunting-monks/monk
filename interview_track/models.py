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
APPLICATION_STATUS_MAP = utils.list2map(APPLICATION_STATUS)
APPLICATION_STATUS_DICT = utils.list2dict(APPLICATION_STATUS)

INTERVIEW_CATEGORIES = (
    ('', 'Interview type'),
    (1, 'Phone screen'),
    (2, 'Onsite'),
    (3, 'Onsite with HR'),
    (4, 'Onsite with HM'))
INTERVIEW_CATEGORIES_MAP = utils.list2map(INTERVIEW_CATEGORIES)
INTERVIEW_CATEGORIES_DICT = utils.list2dict(INTERVIEW_CATEGORIES)

INTERVIEW_STATUS = (
    (1, 'Scheduled'),
    (2, 'Candidate Confirmed'),
    (3, 'Interviewer Confirmed'),
    (4, 'Passed'),
    (5, 'Rejected'))
INTERVIEW_STATUS_MAP = utils.list2map(INTERVIEW_STATUS)
INTERVIEW_STATUS_DICT = utils.list2dict(INTERVIEW_STATUS)


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


class ScoreCardTemplate(models.Model):
    name = models.CharField(max_length=100, unique=True, default="")
    field1 = models.CharField(max_length=500, default="")
    field2 = models.CharField(max_length=500, blank=True, default="")
    field3 = models.CharField(max_length=500, blank=True, default="")
    field4 = models.CharField(max_length=500, blank=True, default="")
    field5 = models.CharField(max_length=500, blank=True, default="")
    field6 = models.CharField(max_length=500, blank=True, default="")
    field7 = models.CharField(max_length=500, blank=True, default="")
    field8 = models.CharField(max_length=500, blank=True, default="")
    field9 = models.CharField(max_length=500, blank=True, default="")
    field10 = models.CharField(max_length=500, blank=True, default="")
    created_by = models.ForeignKey(Employee)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%d: %s" % (self.id, self.name)


class Interview(models.Model):
    class meta:
        unique_together = (("case", "interviewer"))

    case = models.ForeignKey(ApplicationCase)
    template = models.ForeignKey(ScoreCardTemplate)
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

    def __unicode__(self):
        return "%s: %s" % (self.case.__unicode__(), self.interviewer.__unicode__())


class InterviewScore(models.Model):

    interview = models.OneToOneField(Interview)
    score1 = models.SmallIntegerField(default=0)
    score2 = models.SmallIntegerField(blank=True, default=0)
    score3 = models.SmallIntegerField(blank=True, default=0)
    score4 = models.SmallIntegerField(blank=True, default=0)
    score5 = models.SmallIntegerField(blank=True, default=0)
    score6 = models.SmallIntegerField(blank=True, default=0)
    score7 = models.SmallIntegerField(blank=True, default=0)
    score8 = models.SmallIntegerField(blank=True, default=0)
    score9 = models.SmallIntegerField(blank=True, default=0)
    score10 = models.SmallIntegerField(blank=True, default=0)
    comment = models.CharField(max_length=2000, blank=True, default="")
    scored_by = models.ForeignKey(Employee)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode(self):
        return "%s: %s" % (self.interview.__unicode__(), self.scored_by.__unicode__())
