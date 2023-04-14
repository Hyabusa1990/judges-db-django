from django.urls import path
from judge.views import details

urlpatterns = [
    path("<pk>/", details, name="judge.details")
]
