from django.contrib import admin
from models import Company
from models import Employee
from models import Role
from models import UserDetail
from models import Applicant


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'businessDescription', 'area')
    list_display_links = ('name',)
    ordering = ['name', ]


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company', 'email')
    list_display_links = ('first_name',)
    ordering = ['first_name', 'last_name']


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    ordering = ['name', ]


class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_display_links = ('user',)


class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'current_company', 'current_title', 'email')
    list_display_links = ('first_name',)
    ordering = ['first_name', 'last_name']


admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(UserDetail, UserDetailAdmin)

# Register your models here.
