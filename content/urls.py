from django.urls import path
from .views import projects_list, project_new

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('', projects_list, name='projects_list'),

  path('new/', project_new, name='project_new'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)