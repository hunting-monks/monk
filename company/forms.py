from django.forms import DateField
from django.forms import ModelChoiceField
from django.forms import ModelForm

from models import Applicant
from models import Employee
from interview_track.models import Job


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


class UserChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s%s" % (obj.last_name, obj.first_name)


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
            'creator',
            'recruiter',
            'hiring_manager')

    def __init__(self, *args, **kwargs):
        company = kwargs.pop('cid', '')
        super(JobForm, self).__init__(*args, **kwargs)
        if not company:
            return
        self.fields['recruiter'] = UserChoiceField(
            queryset=Employee.objects.filter(company=company))
        self.fields['hiring_manager'] = UserChoiceField(
            queryset=Employee.objects.filter(company=company))

