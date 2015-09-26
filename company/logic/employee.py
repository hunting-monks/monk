from company.models import Employee
from company.models import Role


user2employee = {}
def get_employee_by_user(userid):
    try:
        if userid not in user2employee:
            user2employee[userid] = Employee.objects.get(user_id=userid)
        return user2employee[userid]
    except Exception as ex:
        print ex
        return None


role_dict = {}
def get_role(name):
    try:
        if name not in role_dict:
            roles = Role.objects.all()
            for r in roles:
                role_dict[r.name] = r.id
        return role_dict[name]
    except Exception as ex:
        print ex
        return None


company2interviewers = {}
def get_interviewers_by_recruiter(userid):
    """given a recruiter's userid, return all interviewers in
    this recruiter's company"""
    try:
        if userid not in company2interviewers:
            emp = get_employee_by_user(userid)
            if not emp:
                return None
            role = get_role("Interviewer")
            if not role:
                return None
            company2interviewers[userid] = Employee.objects.filter(
                company=emp.company.id, role=role)  # hack: hardcode role number for now
        return company2interviewers[userid]
    except Exception as ex:
        print ex
        return None


uid2role = {}
def get_user_role(uid):
    """given a userid, return the role of this user"""
    try:
        if uid not in uid2role:
            role = Employee.objects.get(user_id=uid).role.name
            uid2role[uid] = role
        return uid2role[uid]
    except Exception as ex:
        print ex
        return None
