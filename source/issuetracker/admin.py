from django.contrib import admin
from issuetracker.models.issues import Issue
from issuetracker.models.statuses import StatusIssue
from issuetracker.models.types_issue import TypeIssue


class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status_id', 'created_at')
    list_filter = ('id', 'title', 'status_id', 'created_at')
    search_fields = ('title', 'description', 'status_id', 'type_issue_id', 'created_at')
    fields = ('title', 'description', 'status', 'type_issue')

admin.site.register(Issue, IssueAdmin)


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

