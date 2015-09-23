from company.models import Applicant


def get_applicants_by_creator(employee_id):
    applicants = Applicant.objects.filter(created_by=employee_id)
    return applicants