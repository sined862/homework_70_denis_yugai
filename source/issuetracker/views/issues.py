from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, View
from issuetracker.models.issues import Issue
from issuetracker.forms import IssueForm
from django.contrib.auth.mixins import LoginRequiredMixin



class IssueView(DetailView):
    template_name = 'issue.html'
    model = Issue



class IssueAddView(LoginRequiredMixin, CreateView):
    template_name = 'issue_add.html'
    form_class = IssueForm
    model = Issue
    

    def get_success_url(self):
        return reverse('issue', kwargs={'pk': self.object.pk})


class IssueUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'issue_update.html'
    form_class = IssueForm
    model = Issue
    pk_url_kwarg = 'pk'
    context_object_name = 'issue'



class IssueDelView(LoginRequiredMixin, DeleteView):
    template_name = 'issue_del.html'
    model = Issue
    success_url = reverse_lazy('index')



class IssueDelConfirmView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        issue.delete()
        return redirect('index')
