from company.models import Employee
from interview_track.models import Job


user2company = {}
def get_jobs_by_user(userid):
    """given a userid, return all jobs posted by the company which this
    user belongs to"""
    if userid not in user2company:
        company = Employee.objects.get(user=userid).company
        user2company[userid] = company.id
    jobs = Job.objects.filter(company=user2company[userid])
    return jobs


eid2company = {}
def get_jobs_by_eid(eid):
    if eid not in eid2company:
        company = Employee.objects.get(pk=eid).company
        eid2company[eid] = company.id
    jobs = Job.objects.filter(company=eid2company[eid])
    return jobs
