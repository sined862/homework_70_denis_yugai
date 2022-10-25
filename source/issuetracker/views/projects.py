from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, ListView, UpdateView
from issuetracker.models.issues import Issue
from issuetracker.forms import ProjectForm, AddUserForm
from issuetracker.models.projects import Project
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class CustomUserPassesTestMixin(UserPassesTestMixin):
    groups = []

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()

class ProjectsView(ListView):
    template_name = 'projects.html'
    model = Project
    context_object_name = 'projects'


class ProjectView(DetailView):
    template_name = 'project.html'
    model = Project
 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        context['issues'] = Issue.objects.filter(project=project)
        return context
    

class ProjectAddView(LoginRequiredMixin, CreateView):
    template_name = 'project_add.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('project', kwargs={'pk': self.object.pk})


class UserAddView(CustomUserPassesTestMixin, LoginRequiredMixin, UpdateView):
    template_name = 'add_user.html'
    form_class = AddUserForm
    model = Project
    pk_url_kwarg = 'pk'
    context_object_name = 'my_users'
    groups = ['manager']

    def get_success_url(self):
        return reverse('project', kwargs={'pk': self.object.pk})
    