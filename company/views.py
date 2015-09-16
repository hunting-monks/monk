from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from logic import applicant
from models import Employee

def candidate_list(request, action=None):
    if request.user.is_authenticated():
        company = Employee.objects.get(user=request.user.id)
        candidates = applicant.get_applicants(company_id=company.company)
    return render_to_response(
                'recruiter_home.html',
                {'candidates': candidates},
                context_instance=RequestContext(request))
