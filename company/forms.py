from django.forms import DateField
from django.forms import ModelForm
from models import Applicant


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

