from django.views.generic import ListView
from issuetracker.models.issues import Issue



class IndexView(ListView):
    template_name = 'index.html'
    model = Issue
    context_object_name = 'issues'
    ordering = ('-created_at',)

    # def get_context_data(self, **kwargs):
    #     kwargs['issues'] = Issue.objects.all().order_by('id').reverse
    #     return super().get_context_data(**kwargs)