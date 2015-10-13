from django.forms import DateField
from django.forms import ModelChoiceField
from django.forms import ModelForm

from company.models import ROLES_MAP
from interview_track.models import ApplicationCase
from interview_track.models import Interview
from interview_track.models import InterviewScore
from interview_track.models import Job
from logic import applicant
from logic import job
from models import Applicant
from models import Employee
from models import Role, Roles


class ApplicantForm(ModelForm):
    graduate_date = DateField(input_formats=['%m/%d/%Y', ])
    class Meta:
        model = Applicant
        fields = (
            'last_name',
            'first_name',
            'current_company',
            'current_title',
            'email',
            'phone',
            'graduate_school',
            'degree',
            'graduate_date',
            'photo',
            'resume',
            'source',
            'created_by')

    def clean_photo(self):
        data = self.cleaned_data['photo']
        if not data:
            data = 'avartars/avartar_default.jpg'
        return data


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = (
            'company',
            'last_name',
            'first_name',
            'title',
            'department',
            'email',
            'phone',
            'role')

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['role'] = ModelChoiceField(queryset=Role.objects.filter(mask__in=(Roles.INTERVIEWER, Roles.RECRUITER)))

    def clean_photo(self):
        data = self.cleaned_data['photo']
        if not data:
            data = 'avartars/avartar_default.jpg'
        return data


class JobForm(ModelForm):
    expire_date = DateField(input_formats=['%m/%d/%Y', ])
    class Meta:
        model = Job
        fields = (
            'company',
            'title',
            'area',
            'level',
            'description',
            'salary_high',
            'salary_low',
            'expire_date',
            'creator',
            'recruiter',
            'hiring_manager')

    def __init__(self, *args, **kwargs):
        cid = kwargs.pop('cid', '')
        super(JobForm, self).__init__(*args, **kwargs)
        if not cid:
            return
        self.fields['recruiter'] = ModelChoiceField(
            queryset=Employee.objects.filter(
            company_id=cid, role__name='Recruiter'))
        self.fields['hiring_manager'] = ModelChoiceField(
            queryset=Employee.objects.filter(
            company_id=cid, role__name='Hiring Manager'))


class ApplicationCaseForm(ModelForm):
    class Meta:
        model = ApplicationCase
        fields = (
            'creator',
            'applicant',
            'job')

    def __init__(self, *args, **kwargs):
        eid = kwargs.pop('eid', '')
        super(ApplicationCaseForm, self).__init__(*args, **kwargs)
        if not eid:
            return
        self.fields['applicant'] = ModelChoiceField(
            queryset=applicant.get_applicants_by_creator(eid))
        self.fields['job'] = ModelChoiceField(
            queryset=job.get_jobs_by_eid(eid))
