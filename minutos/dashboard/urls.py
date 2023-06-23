from django.urls import path, include

urlpatterns = [
    path('projects/', include('project.urls')),
    path('myaccount/', include('userprofile.urls')),
    path('myaccount/teams/', include('team.urls')),



]