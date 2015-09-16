from company.models import Applicant


def get_applicants(company_id):
    applicants = Applicant.objects.filter(created_by_company=company_id)
    return applicants