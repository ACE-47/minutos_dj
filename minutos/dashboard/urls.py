from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('<int:user_id>/view-user/',views.view_user,name='view-user'),    
]