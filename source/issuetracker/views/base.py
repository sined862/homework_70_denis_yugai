﻿from django.views.generic import TemplateView
from issuetracker.models import Issue


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs['issues'] = Issue.objects.all().order_by('id').reverse
        return super().get_context_data(**kwargs)