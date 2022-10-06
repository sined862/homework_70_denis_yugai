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


class IssueUpdateView(View):
    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        form = IssueForm(initial={
            'title': issue.title,
            'description': issue.description,
            'status': issue.status,
            'type_issue': issue.type_issue
        })
        return render(request, 'issue_update.html', context={'form': form, 'issue': issue})

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue.title = form.cleaned_data['title']
            issue.description = form.cleaned_data['description']
            issue.status = form.cleaned_data['status']
            issue.type_issue = form.cleaned_data['type_issue']
            issue.save()
            return redirect('issue', pk=issue.pk)
        else:
            return render(request, 'issue_update.html', context={'form': form, 'issue': issue})


class IssueDelView(View):
    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        return render(request, 'issue_del.html', context={'issue': issue})


class IssueDelConfirmView(View):
    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        issue.delete()
        return redirect('index')
