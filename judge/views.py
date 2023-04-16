from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin


@method_decorator(login_required, name="dispatch")
class JudgeDetailView(UserPassesTestMixin, DetailView):
    model = User
    template_name = "judge/details.html"

    # Check if LoggedIn-User has view permissions
    def test_func(self):
        # if it's own data -> allow
        if self.request.user.pk is self.get_object().pk:
            return True
        # if it's an SuperUser -> allow
        elif self.request.user.is_superuser:
            return True
        # if it's an manager -> allow
        # TODO: check its an manager of the region of the judge
        elif self.request.user.has_perm('judge.view_judge'):
            return True
        # else -> deny
        else:
            return False
