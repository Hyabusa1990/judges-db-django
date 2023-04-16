from django.urls import path
from judge.views import JudgeDetailView, JudgeListView

urlpatterns = [
    # List and Search all Judges
    path("", JudgeListView.as_view(), name="judge.list"),
    # Create new Judge
    path("create/", JudgeDetailView.as_view(), name="judge.create"),
    # Show Details of Judge
    path("<pk>/", JudgeDetailView.as_view(), name="judge.details"),
    # Edit Details of Judge
    path("edit/<pk>/", JudgeDetailView.as_view(), name="judge.edit"),
    # Delete Judge
    path("delete/<pk>/", JudgeDetailView.as_view(), name="judge.delete"),
]
