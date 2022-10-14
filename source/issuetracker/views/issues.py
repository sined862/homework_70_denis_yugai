from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, View
from issuetracker.models.issues import Issue
from issuetracker.forms import IssueForm



class IssueView(DetailView):
    template_name = 'issue.html'
    model = Issue



class IssueAddView(CreateView):
    template_name = 'issue_add.html'
    form_class = IssueForm
    model = Issue

    def get_success_url(self):
        return reverse('issue', kwargs={'pk': self.object.pk})


class IssueUpdateView(UpdateView):
    template_name = 'issue_update.html'
    form_class = IssueForm
    model = Issue
    pk_url_kwarg = 'pk'
    context_object_name = 'issue'
    


class IssueDelView(DeleteView):
    template_name = 'issue_del.html'
    model = Issue
    success_url = reverse_lazy('index')


    # def get(self, request, *args, **kwargs):
    #     issue = get_object_or_404(Issue, pk=kwargs['pk'])
    #     return render(request, 'issue_del.html', context={'issue': issue})


class IssueDelConfirmView(View):
    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        issue.delete()
        return redirect('index')
