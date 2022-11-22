from rest_framework import generics
from issuetracker.models import Issue, Project
from api.serializers import IssueSerializer, ProjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class IssueAPIView(APIView):
    def get(self, request):
        lst = Issue.objects.all().values()
        return Response({'issues': lst})


class IssueDetailAPIView(APIView):
    def get(self, request, pk):
        project = Project.objects.get(pk=pk)
        issues = Issue.objects.filter(project=pk)
        return Response({'project': ProjectSerializer(project).data, 'issues': IssueSerializer(issues, many=True).data})


class UpdateView(APIView):
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT is not allowed'})
        try:
            instance = Project.objects.get(pk=pk)
            print(instance.title)
        except:
            return Response({'error': 'Object does not exists'})

        serializer = ProjectSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'project': serializer.data})


class DeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE is not allowed'})
        project = Project.objects.get(pk=pk)
        project.delete()
        return Response({'project': 'delete'})