from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey

from company.models import Applicant
from company.models import Company
from company.models import Employee


INDUSTRY_CATEGORIES = (
    (1, 'Accounting'),
    (2, 'Computer Hardware'),
    (3, 'Computer Software'),
    (4, 'Internet'))


ROLE_ENUM = (
    (1, 'Admin'),
    (1 << 2, 'Interviewer'),
    (1 << 3, 'HR'),
    (1 << 4, 'Hiring Manager'))


SKILL_LEVEL = (
    (1, 'Entry'),
    (2, 'Junior'),
    (3, 'Senior'),
    (4, 'Veteran'),
    (5, 'Principle'),
    (6, 'Distinguished'))


APPLICANT_SOURCE = (
    (1, 'Internal referral'),
    (2, 'Self submitted'),
    (3, 'Linkedin'))


APPLICATION_STATUS = (
    (1, 'Not started'),
    (2, 'Phone screen scheduled'),
    (3, 'Phone screen finished'),
    (4, 'Onsite scheduled'),
    (5, 'Onsite finished'),
    (6, 'Offered'),
    (7, 'Rejected'),
    (8, 'On hold'))


INTERVIEW_CATEGORIES = (
    (1, 'Phone screen'),
    (2, 'Onsite coding'),
    (3, 'Onsite HR'),
    (4, 'Onsite HM'))


INTERVIEW_STATUS = (
    (1, 'Scheduled'),
    (2, 'Candidate Confirmed'),
    (3, 'Interviewer Confirmed'),
    (4, 'Passed'),
    (5, 'Rejected'))


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

    expire_date = models.DateField(blank=True, default=datetime.min)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ApplicationCase(models.Model):

    applicant = models.ForeignKey(Applicant)
    job = models.ForeignKey(Job)
    status = models.IntegerField(choices=APPLICATION_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)


class Interview(models.Model):

    case = models.ForeignKey(ApplicationCase)
    interviewer = models.ForeignKey(Employee)
    category = models.IntegerField(choices=INTERVIEW_CATEGORIES)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.IntegerField(choices=INTERVIEW_STATUS)
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

