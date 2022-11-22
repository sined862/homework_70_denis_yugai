from rest_framework import generics
from issuetracker.models import Issue
from api.serializers import IssueSerializer

class IssueAPIView(generics.ListAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer