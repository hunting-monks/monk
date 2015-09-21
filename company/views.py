from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import UploadedFile
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import ApplicantForm
from logic import applicant
from models import Employee


@login_required
def list_candidates(request, action=None):
    candidates = {}
    try:
        employee = Employee.objects.get(user=request.user.id)
        candidates = applicant.get_applicants(company_id=employee.company.id)
        candidates = model_to_dict(candidates)
    except Exception as ex:
        print ex
        pass
    return render_to_response(
            'list_candidates.html',
            {'candidates': candidates},
            context_instance=RequestContext(request))


@login_required
def add_candidates(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return render(request, 'candidate_detail.html', {'candi': form.cleaned_data})
            except Exception as ex:
                print ex
    else:
        form = ApplicantForm()

    return render(request, 'add_candidates.html', {'form': form})


@login_required
def candidate_detail(request):
    return


