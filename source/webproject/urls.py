from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.views import IssueAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('issuetracker.urls')),
    path('auth/', include('accounts.urls')),
    path('api/issuelist/', IssueAPIView.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

