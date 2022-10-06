from django.urls import path
from issuetracker.views.base import IndexView
from issuetracker.views.issues import IssueView, IssueAddView, IssueUpdateView, IssueDelView, IssueDelConfirmView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issue/<int:pk>', IssueView.as_view(), name='issue'),
    path('issue_add/', IssueAddView.as_view(), name='issue_add'),
    path('issue_update/<int:pk>', IssueUpdateView.as_view(), name='issue_update'),
    path('issue_del/<int:pk>', IssueDelView.as_view(), name='issue_del'),
    path('issue_del_confirm/<int:pk>', IssueDelConfirmView.as_view(), name='del_confirm')
]