from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import User, Permission
from django.db import models

from common import utils


INDUSTRY_CATEGORIES = (
    (0, 'Unknown'),
    (1, 'Accounting'),
    (2, 'Computer Hardware'),
    (3, 'Computer Software'),
    (4, 'Internet'))
INDUSTRY_CATEGORIES_MAP = utils.list2map(INDUSTRY_CATEGORIES)
INDUSTRY_CATEGORIES_DICT = utils.list2dict(INDUSTRY_CATEGORIES)

ROLES = (
    (0, 'Unknown'),
    (1, 'Admin'),
    (1 << 2, 'Interviewer'),
    (1 << 3, 'Recruiter'),
    (1 << 4, 'Hiring Manager'))
ROLES_MAP = utils.list2map(ROLES)
ROLES_DICT = utils.list2dict(ROLES)

SKILL_LEVEL = (
    (0, 'Unknown'),
    (1, 'Entry'),
    (2, 'Junior'),
    (3, 'Senior'),
    (4, 'Principle'),
    (5, 'Distinguished'))
SKILL_LEVEL_MAP = utils.list2map(SKILL_LEVEL)
SKILL_LEVEL_DICT = utils.list2dict(SKILL_LEVEL)

APPLICANT_SOURCE = (
    (0, 'Unknown'),
    (1, 'Internal referral'),
    (2, 'Self submitted'),
    (3, 'Linkedin'))
APPLICANT_SOURCE_MAP = utils.list2map(APPLICANT_SOURCE)
APPLICANT_SOURCE_DICT = utils.list2dict(APPLICANT_SOURCE)

SEX_CHOICES = (
    (0, 'U'),
    (1, 'M'),
    (2, 'F'))
SEX_CHOICES_MAP = utils.list2map(SEX_CHOICES)
SEX_CHOICES_DICT = utils.list2dict(SEX_CHOICES)

EE_STATUS_CHOICES = (
    ('Ped', 'Pending'),
    ('Act', 'Active'),
    ('Del', 'Deleted'))
EE_STATUS_CHOICES_MAP = utils.list2map(EE_STATUS_CHOICES)
EE_STATUS_CHOICES_DICT = utils.list2dict(EE_STATUS_CHOICES)

MARITAL_CHOICES = (
    ('U', 'Unknown'),
    ('S', 'Single'),
    ('M', 'Married'))
MARITAL_CHOICES_MAP = utils.list2map(MARITAL_CHOICES)
MARITAL_CHOICES_DICT = utils.list2dict(MARITAL_CHOICES)

DEGREE_CHOICES = (
    (0, 'Unknown'),
    (1, 'Below BS'),
    (2, 'BS'),
    (3, 'MS'),
    (4, 'PHD'))
DEGREE_CHOICES_MAP = utils.list2map(DEGREE_CHOICES)
DEGREE_CHOICES_DICT = utils.list2dict(DEGREE_CHOICES)


class Company(models.Model):
    name = models.CharField(verbose_name='Company Name', max_length=200, db_index=True,)
    businessDescription = models.CharField(verbose_name='Business Description', max_length=20, blank=True)
    area = models.IntegerField(choices=INDUSTRY_CATEGORIES, blank=True, default=0)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(verbose_name='Address', max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(verbose_name='Zip', max_length=10, blank=True)
    city = models.CharField(verbose_name='City', max_length=50, blank=True)
    size = models.IntegerField(verbose_name='Size', default=1)
    province = models.CharField(verbose_name='Province', max_length=20, blank=True)
    state = models.CharField(verbose_name='State', max_length=2, blank=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    administrators = models.ManyToManyField(User, related_name='companies')
    administrator = models.OneToOneField(User, related_name='company')

    @classmethod
    def register_company(cls, user, name, zipCode, phone, size):
        company = Company()
        company.administrator = user
        company.name = name
        company.zip = zipCode
        company.phone = phone
        company.size = size
        company.save()

        # TODO: add role/permission

        user.first_name, user.last_name = 'Admin', 'Monk'
        user.save()
        company.administrators.add(user)

        # create a employee obj for the admin
        Employee.objects.create(company=company,
                                user=user,
                                first_name=user.first_name,
                                last_name=user.last_name,
                                email=user.email,
                                )
        return company


    def __unicode__(self):
        return self.name


class Role(models.Model):

    name = models.CharField(max_length=30, unique=True)
    permission = models.BigIntegerField()
    mask = models.BigIntegerField(choices=ROLES)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    @classmethod
    def create_admin_role(cls):
        role = Role(name='admin')
        # TODO: other props.
        return role

class UserDetail(models.Model):

    user = models.ForeignKey(User)
    company = models.ForeignKey(Company)
    role = models.ForeignKey(Role)
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

    # lets not use role now, we can use group/permission instead.
    # role = models.ForeignKey('Role', related_name='employee', null=True)

    first_name = models.CharField(max_length=50, db_index=True)
    last_name = models.CharField(max_length=50, db_index=True)
    email = models.CharField(max_length=254, blank=True, unique=True)
    middleInitial = models.CharField(max_length=1, blank=True, default="")
    address = models.CharField(max_length=100, blank=True, default="")
    address2 = models.CharField(max_length=100, blank=True, default="")
    city = models.CharField(max_length=35, blank=True, default="")
    state = models.CharField(max_length=2, blank=True, default="")
    zip = models.CharField(max_length=10, blank=True, default="")
    phone = models.CharField(max_length=25, blank=True, default="")

    # shenfenzheng or ssn
    socialId = models.CharField(max_length=128, blank=True, default="")
    dob = models.CharField(max_length=10, blank=True, default="")
    sex = models.IntegerField(choices=SEX_CHOICES, blank=True, default=0)
    marital_status = models.CharField(max_length=2, verbose_name="Marital Status", choices=MARITAL_CHOICES, null=True, blank=True, default='U')
    isDisabled = models.BooleanField(verbose_name="Is Disabled?", default=False)
    ageRange = models.CharField(max_length=8, blank=True, default="")  # Used for manually entered employees only.
    title = models.CharField(max_length=254, blank=True, default="")
    department = models.CharField(max_length=128, default="")

    status = models.CharField(max_length=3, choices=EE_STATUS_CHOICES, default='Act')  # Active, LOA, Terminated
    photo = models.CharField(max_length=255, blank=True, default="")
    deleted = models.BooleanField(blank=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    isRegistered = models.BooleanField(blank=True, default=False)

    def __unicode__(self):
        return "%s %s - %s" % (self.first_name, self.last_name, self.company.name)


class Applicant(models.Model):

    user = models.OneToOneField(User, related_name="user", blank=True, null=True)

    first_name = models.CharField(max_length=50, db_index=True)
    last_name = models.CharField(max_length=50, db_index=True)
    email = models.EmailField(blank=True, unique=True)
    middleInitial = models.CharField(max_length=1, blank=True, default="")
    address = models.CharField(max_length=100, blank=True, default="")
    address2 = models.CharField(max_length=100, blank=True, default="")
    city = models.CharField(max_length=35, blank=True)
    state = models.CharField(max_length=2, blank=True, default="")
    zip = models.CharField(max_length=10, blank=True, default="")
    phone = models.CharField(max_length=25, blank=True, default="")
    photo = models.ImageField(upload_to='avartars/', blank=True, default="")

    area = models.IntegerField(choices=INDUSTRY_CATEGORIES, blank=True, default=0)
    level = models.IntegerField(choices=SKILL_LEVEL, blank=True, default=0)
    expected_salary = models.IntegerField(blank=True, default=0)
    current_salary = models.IntegerField(blank=True, default=0)
    resume = models.FileField(upload_to='resumes/', blank=True, default="")

    current_company = models.CharField(max_length=200)
    current_title = models.CharField(max_length=50)
    current_start_date = models.DateField(blank=True, default=datetime.min)
    current_end_date = models.DateField(blank=True, default=datetime.min)

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
    degree = models.IntegerField(choices=DEGREE_CHOICES)
    graduate_date = models.DateField(blank=True, default=datetime.min)

    graduate_school2 = models.CharField(max_length=50, blank=True, default="")
    degree2 = models.IntegerField(choices=DEGREE_CHOICES, default=0)
    graduate_date2 = models.DateField(blank=True, default=datetime.min)

    graduate_school3 = models.CharField(max_length=50, blank=True, default="")
    degree3 = models.IntegerField(choices=DEGREE_CHOICES, default=0)
    graduate_date3 = models.DateField(blank=True, default=datetime.min)

    source = models.IntegerField(choices=APPLICANT_SOURCE)
    source_id = models.BigIntegerField(default=0)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(Employee, related_name="author")

    def __unicode__(self):
        return "%d: %s%s - %s" % (self.id, self.last_name, self.first_name, self.email)
