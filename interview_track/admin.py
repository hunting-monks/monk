from django.contrib import admin
from models import ApplicationCase
from models import Interview
from models import InterviewScore
from models import Job
from models import ScoreCardTemplate


class ApplicationCaseAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'job', 'status')
    list_display_links = ('applicant',)
    ordering = ['applicant', 'job']


class InterviewAdmin(admin.ModelAdmin):
    list_display = ('case', 'interviewer')
    list_display_links = ('case',)
    ordering = ['case', 'interviewer']


class ScoreCardTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'field1', 'field2', 'field3', 'field4', 'field5')
    list_display_links = ('name',)
    ordering = ['name', ]


class InterviewScoreAdmin(admin.ModelAdmin):
    list_display = ('interview', 'template', 'score1', 'score2', 'score3', 'score4', 'score5')
    list_display_links = ('interview',)
    ordering = ['interview', 'template']


class JobAdmin(admin.ModelAdmin):
    list_display = ('company', 'title')
    list_display_links = ('title',)
    ordering = ['company', 'title']

admin.site.register(ApplicationCase, ApplicationCaseAdmin)
admin.site.register(Interview, InterviewAdmin)
admin.site.register(InterviewScore, InterviewScoreAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(ScoreCardTemplate, ScoreCardTemplateAdmin)

# Register your models here.
