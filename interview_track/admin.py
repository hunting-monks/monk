from django.contrib import admin
from models import ApplicationCase
from models import Interview
from models import InterviewScore
from models import Job


class ApplicationCaseAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'job', 'status')
    list_display_links = ('applicant',)
    ordering = ['applicant', 'job']


class InterviewAdmin(admin.ModelAdmin):
    list_display = ('case', 'interviewer')
    list_display_links = ('case',)
    ordering = ['case', 'interviewer']


class InterviewScoreAdmin(admin.ModelAdmin):
    list_display = ('interview', 'evaluated_field', 'score')
    list_display_links = ('interview',)
    ordering = ['interview', 'evaluated_field']


class JobAdmin(admin.ModelAdmin):
    list_display = ('company', 'title')
    list_display_links = ('title',)
    ordering = ['company', 'title']

admin.site.register(ApplicationCase, ApplicationCaseAdmin)
admin.site.register(Interview, InterviewAdmin)
admin.site.register(InterviewScore, InterviewScoreAdmin)
admin.site.register(Job, JobAdmin)

# Register your models here.
