from rest_framework import generics
from issuetracker.models import Issue
from api.serializers import IssueSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class IssueAPIView(APIView):
    def get(self, request):
        lst = Issue.objects.all().values()
        return Response({'issues': lst})


class IssueDetailAPIView(APIView):
    def get(self, request, pk):
        lst = Issue.objects.filter(project=pk).values()
        return Response({'issues': lst})