from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('',views.projects, name='projects'),
    path('<int:project_id>/project-detail/',views.project_detail, name='project-detail'),
    path('<int:project_id>/edit-project/',views.edit_project, name='edit-project'),
    path('<int:project_id>/<int:task_id>/detail/',views.task_detail, name='task-detail'),
    path('<int:project_id>/<int:task_id>/edit/',views.edit_task, name='edit-task'),
    path('<int:project_id>/<int:task_id>/<int:entry_id>/edit/',views.edit_entry, name='edit-entry'),
    path('<int:project_id>/<int:task_id>/<int:entry_id>/delete/',views.delete_entry, name='delete-entry'),
    path('delete-untracked-entry/<int:entry_id>/',views.delete_untracked_entry, name='delete-untracked-entry'),
    path('track-entry/<int:entry_id>/',views.track_entry, name='track-entry'),



    # API
    
    path('api/start-timer/',api.api_start_timer, name='start-timer'),
    path('api/stop-timer/',api.api_stop_timer, name='stop-timer'),
    path('api/discard-timer/',api.api_discard_timer, name='discard-timer'),
    path('api/get-tasks/',api.api_get_tasks, name='get-tasks'),



]