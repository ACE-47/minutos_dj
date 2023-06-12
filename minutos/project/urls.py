from django.urls import path
from . import views
urlpatterns = [
    path('',views.projects, name='projects'),
    path('<int:project_id>/project-detail/',views.project_detail, name='project-detail'),
    path('<int:project_id>/edit-project/',views.edit_project, name='edit-project'),


]