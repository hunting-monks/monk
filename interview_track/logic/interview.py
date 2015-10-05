from interview_track.models import Interview


def get_interviews_by_user(uid, conditions):
    """ Given a user id, return all interviews where the user is one of
    interviewers"""
    try:
        interviews = Interview.objects.filter(
            interviewer__user_id=uid, *conditions)
    except Exception as ex:
        print ex

    return interviews
