from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

INDUSTRY_CATEGORIES = (
    (1, 'Accounting'),
    (2, 'Computer Hardware'),
    (3, 'Computer Software'),
    (4, 'Internet'))


ROLE_ENUM = (
    (1, 'Admin'),
    (1<<2, 'Interviewer'),
    (1<<3, 'HR'),
    (1<<4, 'Hiring Manager'))


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


class Company(models.Model):
    name = models.CharField(verbose_name='Company Name', max_length=200)
    businessDescription = models.CharField(verbose_name='Business Description', max_length=20, blank=True)
    area = models.IntegerField(choices=INDUSTRY_CATEGORIES)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(verbose_name='Address', mmax_length=50, blank=True)
    address2 = models.CharField(max_length=50)
    zipcode = models.CharField(verbose_name='Zip', max_length=10)
    city = models.CharField(verbose_name='City', max_length=50)
    province = models.CharField(verbose_name='Province', max_length=20)
    state = models.CharField(verbose_name='State', max_length=2, blank=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Role(models.Model):

    name = models.CharField(max_length=30)
    permission = models.BigIntegerField()
    mask = models.BigIntegerField(choices=ROLE_ENUM)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Job(models.Model):
        
    company_id = models.ForeignKey(Company)
    title = models.CharField(max_length=50)
    area = models.IntegerField(choices=INDUSTRY_CATEGORIES)
    level = models.IntegerField(choices=SKILL_LEVEL)
    description = models.CharField(max_length=5000)
    salary_high = models.IntegerField()
    salary_low = models.IntegerField()
    creator_id = models.ForeignKey(User, related_name="creator")
    recruiter_id = models.ForeignKey(User, related_name="recruiter")
    hiring_manager_id = models.ForeignKey(User, related_name="hm")
    expire_date = models.DateField()
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserDetail(models.Model):
        
    user_id = models.ForeignKey(User)
    company_id = models.ForeignKey(Company)
    role_id = models.ForeignKey(Role)
    phone = models.CharField(max_length=20)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Applicant(models.Model):
        
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    area = models.IntegerField(choices=INDUSTRY_CATEGORIES)
    level = models.IntegerField(choices=SKILL_LEVEL)
    expected_salary = models.IntegerField()
    current_salary = models.IntegerField()
    resume_path = models.CharField(max_length=100)
    
    current_company = models.CharField(max_length=200)
    current_title = models.CharField(max_length=50)
    current_start_date = models.DateField()
    current_end_date = models.DateField()
    
    prev_company1 = models.CharField(max_length=200)
    prev_title1 = models.CharField(max_length=50)
    prev_start_date1 = models.DateField()
    prev_end_date1 = models.DateField()
    
    prev_company2 = models.CharField(max_length=200)
    prev_title2 = models.CharField(max_length=50)
    prev_start_date2 = models.DateField()
    prev_end_date2 = models.DateField()
    
    prev_company3 = models.CharField(max_length=200)
    prev_title3 = models.CharField(max_length=50)
    prev_start_date3 = models.DateField()
    prev_end_date3 = models.DateField()    
    
    graduate_school = models.CharField(max_length=50)
    degree = models.CharField(max_length=10)
    graduate_date = models.DateField()
    
    graduate_school2 = models.CharField(max_length=50)
    degree2 = models.CharField(max_length=10)
    graduate_date2 = models.DateField()
    
    graduate_school3 = models.CharField(max_length=50)
    degree3 = models.CharField(max_length=10)
    graduate_date3 = models.DateField()
    
    source = models.IntegerField(choices=APPLICANT_SOURCE)
    source_id =models.BigIntegerField(default=0)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ApplicateCase(models.Model):
        
    applicant_id = models.ForeignKey(Applicant)
    job_id = models.ForeignKey(Job)
    status = models.IntegerField(choices=APPLICATION_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class  Interview(models.Model):

    case_id = models.ForeignKey(ApplicateCase)
    interviewer_id = models.ForeignKey(User)
    category = models.IntegerField(choices=INTERVIEW_CATEGORIES)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.IntegerField(choices=INTERVIEW_STATUS)
    comment = models.CharField(max_length=2000)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class InterviewScore(models.Model):
    
    interview_id = models.ForeignKey(Interview)
    evaluated_field = models.CharField(max_length=50)
    score = models.IntegerField()
    comment = models.CharField(max_length=2000)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    