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
    pass


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company')
    list_display_links = ('first_name',)
    ordering = ['first_name', 'last_name']
    pass


class RoleAdmin(admin.ModelAdmin):
    pass


class UserDetailAdmin(admin.ModelAdmin):
    pass


class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'current_company', 'current_title')
    list_display_links = ('first_name',)
    ordering = ['first_name', 'last_name']
    pass


admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(UserDetail, UserDetailAdmin)

# Register your models here.
