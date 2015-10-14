from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

class AccessAuthorizationMixin(object):
    """
    this verifies that the logged in user has the specified
    permissions.
    """
    # required_roles = (Roles.ADMIN, Roles.RECRUITER, )
    required_roles = ()
    #TODO: will replace roles with permission in the future.
    required_permissions = ()

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        from company.models import Employee
        # if not request.user.has_perms(self.required_permissions):
        employee = Employee.inRequest(request)
        if not employee.role.mask in self.required_roles:
            from django.conf import settings
            return redirect(settings.LOGIN_URL)

        return super(AccessAuthorizationMixin, self).dispatch(request, *args, **kwargs)


