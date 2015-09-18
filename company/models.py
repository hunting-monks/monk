from django.contrib.auth.models import User
from django.db import models

from datetime import datetime

# Create your models here.

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


SEX_CHOICES = (
    (1, 'M'),
    (2, 'F'),
)


EE_STATUS_CHOICES = (
    ('Ped', 'Pending'),
    ('Act', 'Active'),
    ('Del', 'Deleted')
)

MARITAL_CHOICES = (
    ('S', 'Single'),
    ('M', 'Married'),
)


class Company(models.Model):
    name = models.CharField(verbose_name='Company Name', max_length=200)
    businessDescription = models.CharField(verbose_name='Business Description', max_length=20, blank=True)
    area = models.IntegerField(choices=INDUSTRY_CATEGORIES)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(verbose_name='Address', max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(verbose_name='Zip', max_length=10, blank=True)
    city = models.CharField(verbose_name='City', max_length=50)
    province = models.CharField(verbose_name='Province', max_length=20)
    state = models.CharField(verbose_name='State', max_length=2, blank=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    administrators = models.ManyToManyField(User, related_name='companies')
    administrator = models.OneToOneField(User, related_name='company')

    def __unicode__(self):
        return self.name


class Role(models.Model):

    name = models.CharField(max_length=30)
    permission = models.BigIntegerField()
    mask = models.BigIntegerField(choices=ROLE_ENUM)
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


class Employee(models.Model):
    class Meta:
        unique_together = (
            ("user",)
        )

    user = models.OneToOneField(User, null=True)

    company = models.ForeignKey('Company', related_name='employees')

    first_name = models.CharField(max_length=50, db_index=True)
    last_name = models.CharField(max_length=50, db_index=True)
    email = models.CharField(max_length=254, blank=True, db_index=True)
    middleInitial = models.CharField(max_length=1, blank=True)
    address = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=35, blank=True)
    state = models.CharField(max_length=2, blank=True, default="")
    zip = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=25, blank=True)

    # shenfenzheng or ssn
    socialId = models.CharField(max_length=128, blank=True, default="")
    dob = models.CharField(max_length=10, blank=True, default="")
    sex = models.IntegerField(choices=SEX_CHOICES, blank=True)
    marital_status = models.CharField(max_length=2, verbose_name="Marital Status", choices=MARITAL_CHOICES, null=True, blank=True)
    isDisabled = models.BooleanField(verbose_name="Is Disabled?", default=False)
    ageRange = models.CharField(max_length=8, blank=True, default="")  # Used for manually entered employees only.
    title = models.CharField(max_length=254, blank=True, default="")
    department = models.CharField(max_length=128, default="")

    status = models.CharField(max_length=3, choices=EE_STATUS_CHOICES)  # Active, LOA, Terminated
    photoUrl = models.CharField(max_length=255, blank=True, default="")

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.company.name


class Applicant(models.Model):

    user = models.OneToOneField(User, related_name="user", blank=True, null=True)

    first_name = models.CharField(max_length=50, db_index=True)
    last_name = models.CharField(max_length=50, db_index=True)
    email = models.EmailField(blank=True, db_index=True)
    middleInitial = models.CharField(max_length=1, blank=True, default="")
    address = models.CharField(max_length=100, blank=True, default="")
    address2 = models.CharField(max_length=100, blank=True, default="")
    city = models.CharField(max_length=35, blank=True)
    state = models.CharField(max_length=2, blank=True, default="")
    zip = models.CharField(max_length=10, blank=True, default="")
    phone = models.CharField(max_length=25, blank=True, default="")

    area = models.IntegerField(choices=INDUSTRY_CATEGORIES)
    level = models.IntegerField(choices=SKILL_LEVEL)
    expected_salary = models.IntegerField()
    current_salary = models.IntegerField()
    resume_path = models.CharField(max_length=100)

    current_company = models.CharField(max_length=200)
    current_title = models.CharField(max_length=50)
    current_start_date = models.DateField()
    current_end_date = models.DateField()

    prev_company1 = models.CharField(max_length=200, blank=True, default="")
    prev_title1 = models.CharField(max_length=50, blank=True, default="")
    prev_start_date1 = models.DateField(blank=True, default=datetime.min)
    prev_end_date1 = models.DateField(blank=True, default=datetime.min)

    prev_company2 = models.CharField(max_length=200, blank=True, default="")
    prev_title2 = models.CharField(max_length=50, blank=True, default="")
    prev_start_date2 = models.DateField(blank=True, default=datetime.min)
    prev_end_date2 = models.DateField(blank=True, default=datetime.min)

    prev_company3 = models.CharField(max_length=200, blank=True, default="")
    prev_title3 = models.CharField(max_length=50, blank=True, default="")
    prev_start_date3 = models.DateField(blank=True, default=datetime.min)
    prev_end_date3 = models.DateField(blank=True, default=datetime.min)

    graduate_school = models.CharField(max_length=50)
    degree = models.CharField(max_length=10)
    graduate_date = models.DateField()

    graduate_school2 = models.CharField(max_length=50, blank=True, default="")
    degree2 = models.CharField(max_length=10, blank=True, default="")
    graduate_date2 = models.DateField(blank=True, default=datetime.min)

    graduate_school3 = models.CharField(max_length=50, blank=True, default="")
    degree3 = models.CharField(max_length=10, blank=True, default="")
    graduate_date3 = models.DateField(blank=True, default=datetime.min)

    source = models.IntegerField(choices=APPLICANT_SOURCE)
    source_id = models.BigIntegerField(default=0)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(Employee, related_name="author")
