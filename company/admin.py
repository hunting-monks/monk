from django.contrib import admin
from django.contrib.auth.models import Permission
from models import Company
from models import Employee
from models import Role
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


class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'current_company', 'current_title', 'email')
    list_display_links = ('first_name',)
    ordering = ['first_name', 'last_name']

class PermissionAdmin(admin.ModelAdmin):
    model = Permission
    fields = ['name', 'content_type', 'codename']

admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Permission, PermissionAdmin)

# Register your models here.
