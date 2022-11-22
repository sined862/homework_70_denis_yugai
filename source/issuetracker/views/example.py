import json
from datetime import datetime
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from issuetracker.models.issues import Issue

def echo(request, *args, **kwargs):
    answer = {
        'time': datetime.now().strftime('%Y-%m-%d %h: %M: %S'),
        'method': request.method
    }
    if request.body:
        answer['answer'] = json.loads(request.body)
    return JsonResponse(answer)

@ensure_csrf_cookie
def get_token(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(f'Not allowed {request.method}')


def json_issues(request, *args, **kwargs):
    if request.method == 'GET':
        fields = ('pk', 'title', 'description', 'status', 'type_issue')
        issues = Issue.objects.values(*fields)
        return JsonResponse(list(issues), safe=False)
    if request.method == 'POST' and request.body:
        issue = json.loads(request.body)
        try:
            response_data = Issue.objects.create(**issue)
            response = JsonResponse({"id"})
            response.status_code = 201
        except Exception as e:
            print(e)
            raise
            response_data = {"detail": "Неккоректный набор полей"}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response
