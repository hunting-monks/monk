from company.logic import employee
from interview_track.models import ApplicationCase


def get_application_cases_by_uid(uid, conditions=[]):
    """Given a user id, get all application cases that belong to the Company
    where the user is in"""
    cid = employee.get_employee_by_user(userid=uid).company.id
    return ApplicationCase.objects.filter(job__company_id=cid, *conditions)