from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, TemplateView
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
        elif self.request.user.has_perm('judge.view_judge') and self.request.user.judge.managed_regions.filter(pk=self.get_object().judge.region.pk).exists():
            return True
        # else -> deny
        else:
            return False


@method_decorator(permission_required('judge.view_judge'), name="dispatch")
class JudgeListView(TemplateView):
    template_name = "judge/list.html"
