from django.urls import path
from api.views import IssueDetailAPIView, DeleteView, UpdateView


urlpatterns = [
    path('projects/detail/<int:pk>', IssueDetailAPIView.as_view()),
    path('projects/update/<int:pk>', UpdateView.as_view()),
    path('projects/delete/<int:pk>', DeleteView.as_view())
]