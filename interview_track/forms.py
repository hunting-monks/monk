from django.forms import ChoiceField
from django.forms import DateField
from django.forms import ModelChoiceField
from django.forms import ModelForm
from django.forms import TimeField

from company.models import Employee
from models import Interview
from models import ScoreCardTemplate
from models import InterviewScore


class InterviewForm(ModelForm):
    interview_date = DateField(input_formats=['%m/%d/%Y', ])
    start_time = TimeField(input_formats=['%I:%M%p'])
    end_time = TimeField(input_formats=['%I:%M%p'])
    class Meta:
        model = Interview
        fields = (
            'case',
            'template',
            'category',
            'interviewer',
            'interview_date',
            'start_time',
            'end_time')

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
        self.fields['template'] = ModelChoiceField(
            queryset=ScoreCardTemplate.objects.filter(created_by__company=cid),
            empty_label="Select a score card template")


class ScoreCardTemplateForm(ModelForm):
    class Meta:
        model = ScoreCardTemplate
        fields = (
            'name',
            'field1',
            'field2',
            'field3',
            'field4',
            'field5',
            'field6',
            'field7',
            'field8',
            'field9',
            'field10',
            'created_by')


class InterviewScoreForm(ModelForm):
    class Meta:
        model = InterviewScore
        fields = (
            'score1',
            'score2',
            'score3',
            'score4',
            'score5',
            'score6',
            'score7',
            'score8',
            'score9',
            'score10',
            'comment',
            'scored_by')
