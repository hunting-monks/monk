from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import User, Permission
from django.db import models
try:
    from django.contrib.sites.shortcuts import get_current_site
except ImportError:
    from django.contrib.sites.models import get_current_site

from common import utils
from registration.models import RegistrationProfile
from django.contrib.sites.models import Site


INDUSTRY_CATEGORIES = (
    (0, 'Unknown'),
    (1, 'Accounting'),
    (2, 'Computer Hardware'),
    (3, 'Computer Software'),
    (4, 'Internet'))
INDUSTRY_CATEGORIES_MAP = utils.list2map(INDUSTRY_CATEGORIES)
INDUSTRY_CATEGORIES_DICT = utils.list2dict(INDUSTRY_CATEGORIES)

class Roles:
    UNKNOWN = 0
    ADMIN = 1
    INTERVIEWER = 4
    RECRUITER = 8
    HIRING_MANAGER = 16

ROLES_CHOICES = (
    (Roles.UNKNOWN, 'Unknown'),
    (Roles.ADMIN, 'Admin'),
    (Roles.INTERVIEWER, 'Interviewer'),
    (Roles.RECRUITER, 'Recruiter'),
    (Roles.HIRING_MANAGER, 'Hiring Manager'))
ROLES_MAP = utils.list2map(ROLES_CHOICES)
ROLES_DICT = utils.list2dict(ROLES_CHOICES)

class Perms:
    READ = 'r'
    WRITE = 'w'
PERMS_CHOICES = (
    (Perms.READ, 'r'),
    (Perms.WRITE, 'w'),
)

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

class EEStatus:
    PED = 'Ped'
    ACT = 'Act'
    INA = 'Ina'
    DEL = 'Del'
EE_STATUS_CHOICES = (
    (EEStatus.PED, 'Pending'),
    (EEStatus.ACT, 'Active'),
    (EEStatus.INA, 'Inactive'),
    (EEStatus.DEL, 'Deleted'))
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

        user.first_name, user.last_name = 'Admin', 'Monk'
        user.save()
        company.administrators.add(user)

        # create a employee obj for the admin
        Employee.objects.create(company=company,
                                user=user,
                                first_name=user.first_name,
                                last_name=user.last_name,
                                email=user.email,
                                role=Role.get_admin_role()
                                )
        return company

    @classmethod
    def inRequest(cls, request):
        return cls.inUser(request.user)

    @classmethod
    def inUser(cls, user):
        if not user.is_authenticated():
            raise Company.DoesNotExist()
        return user.employee.company

    @property
    def interviewers(self):
        return Employee.objects.filter(company=self,
                                       role__mask__in=(Roles.INTERVIEWER, ))

    @property
    def recruiters(self):
        return Employee.objects.filter(company=self,
                                       role__mask__in=(Roles.RECRUITER, ))

    @property
    def activeInterviewers(self):
        return self.interviewers.filter(status=EEStatus.ACT)

    @property
    def activeRecruiters(self):
        return self.recruiters.filter(status=EEStatus.ACT)


    def __unicode__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=30)
    permission = models.CharField(max_length=10, choices=ROLES_CHOICES)
    mask = models.BigIntegerField(choices=PERMS_CHOICES)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    @classmethod
    def get_admin_role(cls):
        role, _ = Role.objects.get_or_create(
            name='admin',
            permission=Perms.WRITE,
            mask=Roles.ADMIN,
		)
        return role

    @classmethod
    def get_recruiter_role(cls):
        role, _ = Role.objects.get_or_create(
            name='recruiter',
            permission=Perms.WRITE,
            mask=Roles.RECRUITER,
		)
        return role

    @classmethod
    def get_interviewer_role(cls):
        role, _ = Role.objects.get_or_create(
            name='interviewer',
            permission=Perms.WRITE,
            mask=Roles.INTERVIEWER,
		)
        return role

    class Meta:
        unique_together = (
            ("name", "permission", "mask", )
        )


class Employee(models.Model):
    class Meta:
        unique_together = (
            ("user",)
        )

    user = models.OneToOneField(User, null=True)
    company = models.ForeignKey('Company', related_name='employees')

    # lets not use role now, we can use group/permission instead.
    role = models.ForeignKey('Role', related_name='employees', null=False)

    first_name = models.CharField(max_length=50, db_index=True)
    last_name = models.CharField(max_length=50, db_index=True)
    email = models.CharField(max_length=254, db_index=True, unique=True)
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

    status = models.CharField(max_length=3, choices=EE_STATUS_CHOICES, default='Ina')  # Active, LOA, Terminated
    photo = models.CharField(max_length=255, blank=True, default="")
    deleted = models.BooleanField(blank=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    isRegistered = models.BooleanField(blank=True, default=False)

    def __unicode__(self):
        return "%s %s - %s" % (self.first_name, self.last_name, self.company.name)

    @classmethod
    def inRequest(cls, request):
        return cls.inUser(request.user)

    @classmethod
    def inUser(cls, user):
        if not user.is_authenticated():
            raise Company.DoesNotExist()
        return user.employee

    @property
    def isRegisteredEmployee(self):
        if not self.user:
            return False
        username = self.user.username
        return not (not '@' in username and len(username) == 30)

    @property
    def isRecruiter(self):
        return self.role.mask in (Roles.RECRUITER, Roles.ADMIN)

    @property
    def isInterviewer(self):
        return self.role.mask in (Roles.INTERVIEWER)


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
