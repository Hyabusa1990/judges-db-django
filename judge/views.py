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

    # Check if LoggedIn-User has view perm or is own
    # TODO: Check if LoggedIn-User is Manager of Judge
    def test_func(self):
        if self.request.user.has_perm('judge.view_judge') or self.request.user.pk is self.get_object().pk:
            return True
        else:
            return False
