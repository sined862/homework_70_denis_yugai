from rest_framework import serializers
from issuetracker.models import *
from rest_framework.renderers import JSONRenderer
from issuetracker.models import Issue


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('title', 'description', 'status', 'type_issue')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'description', 'date_begin', 'date_end', 'date_end')

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.date_begin = validated_data.get('date_begin', instance.date_begin)
        instance.date_end = validated_data.get('date_end', instance.date_end)
        instance.save()
        return instance

    


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
