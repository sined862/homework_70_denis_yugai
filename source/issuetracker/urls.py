from django.urls import path
from issuetracker.views.base import IndexView
from issuetracker.views.issues import IssueView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issue/<int:pk>', IssueView.as_view(), name='issue')
]