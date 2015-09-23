from company.models import Employee
from company.models import UserDetail
from interview_track.models import Job


user2company = {}
def get_jobs_by_user(userid):
    if userid not in user2company:
        company = UserDetail.objects.get(user=userid).company
        user2company[userid] = company.id
    jobs = Job.objects.filter(company=user2company[userid])
    return jobs


eid2company = {}
def get_jobs_by_company(eid):
    if eid not in eid2company:
        company = Employee.objects.get(pk=eid).company
        eid2company[eid] = company.id
    jobs = Job.objects.filter(company=eid2company[eid])
    return jobs