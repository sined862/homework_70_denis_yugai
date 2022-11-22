from rest_framework import serializers
from issuetracker.models import *
from rest_framework.renderers import JSONRenderer
from issuetracker.models import Issue


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('title', 'project')

# class TypeSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100, required=True, allow_blank=False)

# class IssueSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=200, required=True)
#     description = serializers.CharField(max_length=3000, required=True)
#     status = serializers.PrimaryKeyRelatedField(read_only=True)
#     type_issue = TypeSerializer(many=True)
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#     project = serializers.PrimaryKeyRelatedField(read_only=True)
