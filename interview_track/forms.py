from django.forms import ChoiceField
from django.forms import DateField
from django.forms import ModelChoiceField
from django.forms import ModelForm
from django.forms import TimeField

from company.models import Employee
from models import Interview


class InterviewForm(ModelForm):
    interview_date = DateField(input_formats=['%m/%d/%Y', ])
    start_time = TimeField(input_formats=['%I:%M%p'])
    end_time = TimeField(input_formats=['%I:%M%p'])
    class Meta:
        model = Interview
        fields = (
            'case',
            'category',
            'interviewer')

    def __init__(self, *args, **kwargs):
        eid = kwargs.pop('eid', '')
        super(InterviewForm, self).__init__(*args, **kwargs)
        if not eid:
            return
        cid = Employee.objects.get(pk=eid).company.id
        if not cid:
            return
        self.fields['interviewer'] = ModelChoiceField(
            queryset=Employee.objects.filter(company=cid, role__name='Interviewer'),
            empty_label="Select an interviewer")

