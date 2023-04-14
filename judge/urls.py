from django.urls import path
from judge.views import details

urlpatterns = [
    # List and Search all Judges
    path("", details, name="judge.list"),
    # Create new Judge
    path("create/", details, name="judge.create"),
    # Show Details of Judge
    path("<pk>/", details, name="judge.details"),
    # Edit Details of Judge
    path("edit/<pk>/", details, name="judge.edit"),
    # Delete Judge
    path("delete/<pk>/", details, name="judge.delete"),
]
