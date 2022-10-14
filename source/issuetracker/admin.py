from django.contrib import admin
from issuetracker.models.issues import Issue
from issuetracker.models.statuses import StatusIssue
from issuetracker.models.types_issue import TypeIssue
from issuetracker.models.projects import Project


class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status_id', 'created_at', 'project')
    list_filter = ('id', 'title', 'status_id', 'created_at', 'project')
    search_fields = ('title', 'description', 'status_id', 'type_issue_id', 'created_at', 'project')
    fields = ('title', 'description', 'status', 'type_issue', 'project')

admin.site.register(Issue, IssueAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'date_begin', 'date_end')
    list_filter = ('id', 'title', 'date_begin', 'date_end')
    search_fields = ('title', 'description', 'date_begin', 'date_end')
    fields = ('title', 'description', 'date_begin', 'date_end')

admin.site.register(Project, ProjectAdmin)


class StatusIssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    # list_filter = 'title'
    # search_fields = 'title'
    # fields = 'title'

admin.site.register(StatusIssue, StatusIssueAdmin)


class TypeIssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    # list_filter = ('id', 'title')
    # search_fields = ('id', 'title')
    # fields = ('id', 'title')

admin.site.register(TypeIssue, TypeIssueAdmin)

