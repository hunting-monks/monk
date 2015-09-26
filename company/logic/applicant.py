from company.models import Applicant
from company.models import Employee


def get_applicants_by_company(company_id):
    """given a company id, return all applicants created by employees in
    the company"""
    all_employees = Employee.objects.filter(company=company_id)
    if not all_employees:
        return []
    try:
        applicants = Applicant.objects.filter(
            created_by__in=[e.id for e in all_employees])
    except Exception as ex:
        print ex
        return []
    return applicants


def get_applicants_by_creator(employee_id):
    """given an employee id, return all applicants created by all employees
    in the same company"""
    company = Employee.objects.get(pk=employee_id)
    return get_applicants_by_company(company.id)
