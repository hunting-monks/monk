from django.contrib import admin
from models import ApplicationCase
from models import Interview
from models import InterviewScore
from models import Job


class ApplicationCaseAdmin(admin.ModelAdmin):
    pass


class InterviewAdmin(admin.ModelAdmin):
    pass


class InterviewScoreAdmin(admin.ModelAdmin):
    pass


class JobAdmin(admin.ModelAdmin):
    pass


admin.site.register(ApplicationCase, ApplicationCaseAdmin)
admin.site.register(Interview, InterviewAdmin)
admin.site.register(InterviewScore, InterviewScoreAdmin)
admin.site.register(Job, JobAdmin)

# Register your models here.
