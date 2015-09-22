from company.models import Employee


user2employee = {}

def get_employee_by_user(userid):
    if userid in user2employee:
        return user2employee[userid]
    try:
        user2employee[userid] = Employee.objects.get(user_id=userid)
        return user2employee[userid]
    except Exception as ex:
        print ex
        return -1
