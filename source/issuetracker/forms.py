from django import forms
from django.forms import widgets
from issuetracker.models import StatusIssue, TypeIssue


class IssueForm(forms.Form):
    title = forms.CharField(
        max_length=20,
        required=True,
        label='Краткое описание',
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        max_length=800,
        required=False,
        label='Полное описание',
        widget=widgets.Textarea(attrs={'class': 'form-control', 'style': 'height:150px'})
    )
    status = forms.ModelChoiceField(
        queryset=StatusIssue.objects.all(),
        label='Статус',
        widget=forms.RadioSelect
    )
    type_issue = forms.ModelChoiceField(
        queryset=TypeIssue.objects.all(),
        label='Тип',
        widget=forms.RadioSelect
    )