from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View
from issuetracker.models import Issue
from issuetracker.forms import IssueForm


class IssueView(TemplateView):
    template_name = 'issue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        return context


class IssueAddView(View):
    def get(self, request, *args, **kwargs):
        form = IssueForm()
        context = {'form': form}
        return render(request, 'issue_add.html', context)

    def post(self, request, *args, **kwargs):
        form = IssueForm(request.POST)
        if not form.is_valid():
            return render(request, 'issue_add.html', context={'form': form})
        issue = Issue.objects.create(**form.cleaned_data)
        return redirect('issue', pk=issue.pk)