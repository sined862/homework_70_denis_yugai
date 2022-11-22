from django.urls import path
from api.views import IssueDetailAPIView


urlpatterns = [
    path('projects/detail/<int:pk>', IssueDetailAPIView.as_view())
]