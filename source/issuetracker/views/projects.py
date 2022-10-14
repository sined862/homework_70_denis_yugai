from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, View, ListView
from issuetracker.models.issues import Issue
from issuetracker.forms import ProjectForm
from issuetracker.models.projects import Project


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
    

class ProjectAddView(CreateView):
    template_name = 'project_add.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('project', kwargs={'pk': self.object.pk})