from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def details(request, pk):
    usr = get_object_or_404(User, pk=pk)

    # Check if LoggedIn-User has view perm or is own
    # TODO: Check if LoggedIn-User
    if request.user.has_perm('judge.view_judge') or request.user.pk is usr.pk:
        context = {"object": usr}
        return render(request, "judge/details.html", context)
    else:
        return HttpResponseForbidden()
